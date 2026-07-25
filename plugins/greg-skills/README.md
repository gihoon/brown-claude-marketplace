# greg-skills

아이디어 파이프라인과 지식관리 파이프라인을 하나로 묶은 Claude Code 스킬 패키지.

## 스킬 목록

### 아이디어 파이프라인

```
/sharpen → /productify
```

| 스킬 | 설명 |
|------|------|
| `/sharpen` | 모호한 아이디어·요청을 구체적인 명세서로 다듬기 |
| `/productify` | 명세서를 받아 최적 제품 형태 결정 + 페이즈별 로드맵 설계 |

### 지식관리 파이프라인 (Zettelkasten)

```
/raw → /perm → /wiki
          ↓
     /query  /lint
```

| 스킬 | 설명 |
|------|------|
| `/raw` | 임시노트 즉시 저장. `/raw scan`으로 미처리 목록 확인 후 영구노트 전환 |
| `/perm` | 원자적 영구노트 생성. VAULT_INDEX 연결 + cascade.py 후처리 |
| `/wiki` | 클러스터 개념 허브 페이지 생성 |
| `/query` | 볼트 4-Way 검색 (키워드·태그·클러스터·연결 기준) |
| `/lint` | 볼트 건강 점검 (고아 노트, 깨진 링크, 미처리 raw) |

## 디렉터리 구조

```
greg-skills/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   ├── sharpen/SKILL.md
│   ├── productify/SKILL.md
│   ├── raw/SKILL.md
│   ├── perm/SKILL.md
│   │   └── cascade.py
│   ├── wiki/SKILL.md
│   ├── query/SKILL.md
│   │   └── search.py
│   └── lint/SKILL.md
└── README.md
```

## 사용 예시

```
/raw 오늘 미팅에서 나온 아이디어 메모
/sharpen 이 아이디어를 제품 명세로 만들어줘
/productify
/perm 새로운 인사이트 정리
/query 지식관리 관련 노트 찾아줘
```
