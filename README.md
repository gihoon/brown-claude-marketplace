# brown-claude-marketplace

Greg의 Claude Code 스킬 마켓플레이스. 아이디어 파이프라인과 지식관리 파이프라인을 하나의 패키지로 제공합니다.

## 요구사항

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- Claude Pro 이상 (Agent 서브에이전트 사용)

## 설치

```bash
# 마켓플레이스 등록 (최초 1회)
/plugin marketplace add https://github.com/gihoon/brown-claude-marketplace

# 플러그인 설치
/plugin install greg-skills@brown-claude-marketplace
```

## 플러그인 목록

### greg-skills

아이디어 파이프라인 + 지식관리 파이프라인. 총 7개 스킬.

#### 아이디어 파이프라인

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| `/sharpen` | 모호한 아이디어를 구체적인 명세서로 다듬기 | `/sharpen`, `/구체화` |
| `/productify` | 명세서를 받아 페이즈별 로드맵 설계 | `/productify`, `/제품화` |

#### 지식관리 파이프라인 (Zettelkasten)

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| `/raw` | 임시노트 즉시 저장 / `scan`으로 미처리 목록 확인 | `/raw`, `/raw scan` |
| `/perm` | 원자적 영구노트 생성 + VAULT_INDEX 연결 | `/perm` |
| `/wiki` | 클러스터 개념 허브 페이지 생성 | `/wiki` |
| `/query` | 볼트 4-Way 검색 | `/query` |
| `/lint` | 볼트 건강 점검 | `/lint` |

#### 두 파이프라인의 흐름

```
아이디어 떠오름
  │
  ├─ 메모로 남기기 ──→ /raw → /perm → /wiki  (지식 축적)
  │
  └─ 제품으로 만들기 ──→ /sharpen → /productify        (실행 계획)
```

## 업데이트

```bash
/plugin update greg-skills@brown-claude-marketplace
```
