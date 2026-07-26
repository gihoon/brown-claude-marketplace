#!/usr/bin/env python3
"""
Cascade Update Script — /permanent Step 5 토큰 절감용
Claude가 직접 Read/Edit하는 대신 이 스크립트가 일괄 처리.

Usage:
  python3 cascade.py <vault_root> <new_note_path> <new_id> <parent_id> <linked_ids...>

Example:
  python3 cascade.py "/path/to/vault" "2 Permanent/8d. 제목.md" "8d" "8" "6f" "1a1" "5a"
"""
import sys, os, re, json, datetime

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(path, content):
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def add_id_to_links(content, new_id):
    """frontmatter의 links 배열에 new_id 추가 (이미 있으면 스킵)"""
    pattern = r'(links:\s*\[)(.*?)(\])'
    match = re.search(pattern, content)
    if not match:
        return content, False
    existing = match.group(2)
    if f'"{new_id}"' in existing:
        return content, False
    if existing.strip():
        new_links = f'{existing}, "{new_id}"'
    else:
        new_links = f'"{new_id}"'
    return content[:match.start()] + match.group(1) + new_links + match.group(3) + content[match.end():], True

def append_to_vault_index(vault_root, new_id, claim, tags, links, cluster):
    """VAULT_INDEX.md의 해당 클러스터 테이블에 1줄 추가"""
    idx_path = os.path.join(vault_root, '_index', 'VAULT_INDEX.md')
    if not os.path.exists(idx_path):
        return False
    content = read_file(idx_path)
    tags_str = ', '.join(tags) if tags else ''
    links_str = ', '.join(links) if links else ''
    new_row = f'| {new_id} | {claim} | {tags_str} | {links_str} |'
    cluster_header = f'## 클러스터: {cluster}'
    if cluster_header in content:
        lines = content.split('\n')
        insert_idx = None
        for i, line in enumerate(lines):
            if cluster_header in line:
                for j in range(i+1, len(lines)):
                    if lines[j].startswith('## ') or lines[j].startswith('---'):
                        insert_idx = j
                        break
                    if lines[j].startswith('|') and not lines[j].startswith('| ID') and not lines[j].startswith('|--'):
                        insert_idx = j + 1
                if insert_idx is None:
                    insert_idx = len(lines)
                break
        if insert_idx:
            lines.insert(insert_idx, new_row)
            write_file(idx_path, '\n'.join(lines))
            return True
    return False

def update_graph(vault_root, new_id, links):
    """GRAPH.md에 1줄 추가"""
    graph_path = os.path.join(vault_root, '_index', 'GRAPH.md')
    if not os.path.exists(graph_path):
        return False
    content = read_file(graph_path)
    links_str = ', '.join(links) if links else ''
    new_line = f'{new_id} → {links_str}'
    if new_line not in content:
        stats_idx = content.find('## 통계')
        if stats_idx > 0:
            content = content[:stats_idx] + new_line + '\n' + content[stats_idx:]
        else:
            content += '\n' + new_line
        write_file(graph_path, content)
    return True

def update_wiki_page(vault_root, cluster, new_id, claim):
    """해당 클러스터의 wiki 개념 페이지에 새 노트 1줄 추가"""
    if not cluster:
        return False
    wiki_path = os.path.join(vault_root, '1 wiki', f'{cluster}.md')
    if not os.path.exists(wiki_path):
        return False
    content = read_file(wiki_path)

    # 이미 있는지 확인
    if f'[[{new_id}]]' in content:
        return True

    # claim 테이블에 새 행 추가 (테이블 마지막 행 뒤에)
    new_row = f'| [[{new_id}]] | {claim} |'

    # "## 교차 태그" 앞에 삽입
    marker = '## 교차 태그'
    if marker in content:
        content = content.replace(marker, f'{new_row}\n\n{marker}')
    else:
        # 마커 없으면 "## 주요 흐름" 앞에
        marker2 = '## 주요 흐름'
        if marker2 in content:
            content = content.replace(marker2, f'{new_row}\n\n{marker2}')

    # note_count 업데이트
    count_match = re.search(r'note_count:\s*(\d+)', content)
    if count_match:
        old_count = int(count_match.group(1))
        content = content.replace(f'note_count: {old_count}', f'note_count: {old_count + 1}')

    # 본문의 "N개 영구노트" 업데이트
    body_count = re.search(r'(\d+)개 영구노트', content)
    if body_count:
        old = int(body_count.group(1))
        content = content.replace(f'{old}개 영구노트', f'{old + 1}개 영구노트')

    write_file(wiki_path, content)
    return True

def extract_frontmatter_field(content, field):
    """frontmatter에서 특정 필드 값 추출"""
    match = re.search(rf'^{field}:\s*"?(.+?)"?\s*$', content, re.MULTILINE)
    if match:
        return match.group(1).strip('"')
    return ''

def extract_links_array(content):
    match = re.search(r'links:\s*\[(.*?)\]', content)
    if match:
        return [x.strip().strip('"') for x in match.group(1).split(',') if x.strip()]
    return []

def extract_tags_array(content):
    tags = []
    in_tags = False
    for line in content.split('\n'):
        if line.strip().startswith('tags:'):
            in_tags = True
            continue
        if in_tags:
            if line.strip().startswith('- '):
                tags.append(line.strip()[2:].strip())
            elif line.strip() and not line.strip().startswith('-'):
                break
    return tags

def main():
    if len(sys.argv) < 5:
        print("Usage: cascade.py <vault_root> <new_note_path> <new_id> <parent_id> [linked_ids...]")
        sys.exit(1)

    vault_root = sys.argv[1]
    new_note_relpath = sys.argv[2]
    new_id = sys.argv[3]
    parent_id = sys.argv[4]
    linked_ids = sys.argv[5:] if len(sys.argv) > 5 else []

    new_note_path = os.path.join(vault_root, new_note_relpath)
    if not os.path.exists(new_note_path):
        print(f"ERROR: {new_note_path} not found")
        sys.exit(1)

    new_content = read_file(new_note_path)
    claim = extract_frontmatter_field(new_content, 'claim')
    cluster = extract_frontmatter_field(new_content, 'cluster')
    all_links = extract_links_array(new_content)
    tags = extract_tags_array(new_content)
    title = os.path.basename(new_note_path).replace('.md', '').split('. ', 1)[-1] if '. ' in os.path.basename(new_note_path) else os.path.basename(new_note_path).replace('.md', '')

    results = {"cascade": [], "index": {}, "warnings": []}

    # 1. Parent note: add child link
    if parent_id:
        parent_files = [f for f in os.listdir(os.path.join(vault_root, '2 Permanent'))
                       if f.startswith(f'{parent_id}.') or f.startswith(f'{parent_id} ')]
        for pf in parent_files:
            ppath = os.path.join(vault_root, '2 Permanent', pf)
            pcontent = read_file(ppath)
            pcontent, changed = add_id_to_links(pcontent, new_id)
            if changed:
                write_file(ppath, pcontent)
                results["cascade"].append({"path": f"2 Permanent/{pf}", "change": "structural"})

    # 2. Semantic reverse links
    for lid in linked_ids:
        if lid == parent_id:
            continue
        matching = [f for f in os.listdir(os.path.join(vault_root, '2 Permanent'))
                   if f.startswith(f'{lid}.') or f.startswith(f'{lid} ')]
        for mf in matching:
            mpath = os.path.join(vault_root, '2 Permanent', mf)
            mcontent = read_file(mpath)
            mcontent, changed = add_id_to_links(mcontent, new_id)
            if changed:
                write_file(mpath, mcontent)
                results["cascade"].append({"path": f"2 Permanent/{mf}", "change": "semantic"})

    # 3. Index incremental update
    idx_ok = append_to_vault_index(vault_root, new_id, claim, tags, all_links, cluster)
    graph_ok = update_graph(vault_root, new_id, all_links)
    results["index"]["vault_index"] = idx_ok
    results["index"]["graph"] = graph_ok

    # 4. Wiki concept page incremental update
    wiki_ok = update_wiki_page(vault_root, cluster, new_id, claim)
    results["index"]["wiki"] = wiki_ok

    print(json.dumps(results, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
