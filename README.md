# greg-claude-marketplace

Greg의 Claude Code 스킬 마켓플레이스. 아이디어 파이프라인과 지식관리 파이프라인을 하나의 패키지로 제공합니다.

## 출처

이 패키지는 아래 두 소스를 기반으로 통합되었습니다.

- **원본 저장소**: [kimyoon21/brown-claude-marketplace](https://github.com/kimyoon21/brown-claude-marketplace)
- **참고 자료**: [vibelabs.kr/shared/8](https://vibelabs.kr/shared/8)

## 요구사항

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- Claude Pro 이상 (Agent 서브에이전트 사용)

## 설치

```bash
# 마켓플레이스 등록 (최초 1회)
/plugin marketplace add https://github.com/gihoon/brown-claude-marketplace

# 플러그인 설치
/plugin install greg-skills@greg-claude-marketplace
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
/plugin update greg-skills@greg-claude-marketplace
```

---

## 상세 사용법

### /raw — 생각을 즉시 포착

가장 빠른 메모. 분류하거나 정리하지 않고 바로 저장한다.

```
/raw 오늘 떠오른 아이디어: 팀 대시보드를 Slack 대신 Mattermost로 옮기면 어떨까
```

미처리 메모를 모아서 영구노트로 전환하려면:

```
/raw scan
```

→ `0 raw/` 폴더의 미처리 목록을 보여주고, 선택한 항목을 `/perm`으로 연결해준다.

---

### /perm — 아이디어를 영구노트로

생각이 충분히 익었을 때 제텔카스텐에 정식 기록한다.

```
/perm LLM은 검색을 대체하는 게 아니라 검색 결과를 해석하는 레이어다
```

Claude가 VAULT_INDEX를 읽어 연결할 기존 노트를 3개 이하로 추천하고, Folgezettel ID를 배정한 뒤 `cascade.py`로 링크를 자동 업데이트한다.

---

### /wiki — 클러스터 허브 페이지

특정 주제의 노트가 쌓였을 때 한눈에 보이는 인덱스 페이지를 만든다.

```
/wiki AI에이전트
```

---

### /query — 볼트 검색

키워드·태그·클러스터·링크 관계 4가지 방식으로 동시에 검색한다.

```
/query LLM 검색
```

---

### /lint — 볼트 건강 점검

월 1회 정도 돌려서 볼트 상태를 정리한다.

```
/lint
```

고아 노트·깨진 위키링크·미처리 raw 메모·frontmatter 누락을 탐지하고 수정 방향을 제안한다.

---

### /sharpen — 아이디어를 명세서로

막연한 아이디어를 소크라테스식 문답으로 다듬어 제품화 가능한 명세서로 만든다. 개발 착수 전에 쓰면 가장 효과적이다.

```
/sharpen 팀원들이 매일 업무를 정리해서 공유할 수 있는 툴이 있으면 좋겠어
```

Notion 페이지를 입력으로 쓸 수도 있다:

```
/sharpen https://notion.so/xxx
```

**동작 방식**: 최대 10라운드 질문(라운드당 2개 이하) → 명확성 점수 80점 이상이면 명세서 자동 생성.  
판정 축: Who(15) · Why(20) · What(20) · Scope(15) · Measure(15) · Risk(15)

**결과물**: 한 줄 요약 / 대상 / 배경 / 결과물 / 범위 / 성공기준 / 리스크 → Notion 또는 로컬 `.md`

---

### /productify — 명세서를 로드맵으로

명세서를 받아 "어떤 형태의 제품으로 어떻게 만들지"를 설계한다. `/sharpen` 다음 단계로 자연스럽게 이어진다.

```
/productify ./spec-daily-summary.md
```

**핵심 원칙 — 경량화 우선**:
> 가장 가벼운 형태부터 검토한다.  
> `claude-skill → 스크립트 → local HTML → ... → 풀스택 웹서비스`

**보안 판정**:
- 🔴 STOP: 프로덕션 DB 직접 접근, 개인정보 유출 경로 → 보안 담당 리뷰 필수
- 🟡 REVIEW: 테스트 환경 불명확, 민감성 불확실 → 자가 체크 후 진행
- 🟢 SAFE: 공개 API, 익명화 데이터 → 안전 진행

**결과물**: 제품 형태 근거 + 의존성 + Phase별 목표/기준/보안 체크가 담긴 로드맵 문서

---

## 실전 시나리오

### 아이디어 → 지식으로 남기기

```
# 1. 떠오르는 즉시 메모
/raw 팀 대시보드를 Mattermost로 옮기면 알림 피로가 줄 것 같다

# 2. 며칠 후, 정리할 때
/raw scan

# 3. 영구노트로 전환
/perm
```

### 아이디어 → 제품으로 만들기

```
# 1. 명세 다듬기
/sharpen 팀 일일 업무요약 봇을 만들고 싶어

# 2. 로드맵 설계
/productify ./spec.md
```

### 볼트 정기 점검 (월 1회)

```
/lint           # 문제 탐지
/raw scan       # 미처리 메모 정리
/wiki 클러스터명  # 인덱스 갱신
```
