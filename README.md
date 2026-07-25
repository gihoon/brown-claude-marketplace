# greg-claude-marketplace

Greg의 Claude Code 스킬 마켓플레이스. 아이디어 파이프라인과 지식관리 파이프라인을 하나의 패키지로 제공합니다.

## 출처

이 패키지는 아래 두 소스를 기반으로 통합되었습니다.

- **원본 저장소**: [kimyoon21/brown-claude-marketplace](https://github.com/kimyoon21/brown-claude-marketplace)
- **참고 자료**: [vibelabs.kr/shared/8](https://vibelabs.kr/shared/8)

## 요구사항

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- Claude Pro 이상 (Agent 서브에이전트 사용)
- Python 3.9+ (cascade.py, search.py 실행용)
- Obsidian (볼트 뷰어)

## 옵시디언 볼트 준비

스킬을 사용하려면 먼저 옵시디언 볼트가 아래 구조로 준비되어 있어야 한다.

### 스타터킷으로 시작하기 (권장)

원본 스타터킷을 내려받아 Claude Code에게 설치를 맡기는 가장 빠른 방법.

1. [Google Drive에서 zettel-connect-starter.zip 다운로드](https://drive.google.com/file/d/1KCm_BE93x8vh5gg_-fx0YjDkSsIzToFs/view?usp=drive_link)
2. 아래 프롬프트를 Claude Code에 붙여넣기

```
zettel-connect-starter.zip을 사용해서 옵시디언 제텔카스텐 볼트를 설치해줘.
zip 파일 경로와 새 볼트 경로를 물어봐서 진행해줘.
설치 후 SKILL.md 파일 7개의 VAULT_ROOT 경로를 내 볼트 경로로 치환해줘.
```

### 볼트 폴더 구조

```
볼트 루트/
├── 0 raw/            ← /raw 저장 위치 (임시노트)
├── 1 wiki/           ← /wiki 생성 위치 (개념 허브)
├── 2 Permanent/      ← /perm 저장 위치 (영구노트)
├── 3 Archive/        ← 처리 완료된 raw 보관
├── _index/
│   ├── VAULT_INDEX.md   ← 전체 노트 인덱스 (스킬이 자동 관리)
│   └── GRAPH.md         ← 노트 연결 그래프
├── _templates/
├── _attachments/
└── CLAUDE.md         ← 볼트 행동 지침
```

### 핵심: VAULT_ROOT 경로 치환

스킬 설치 후 반드시 7개 SKILL.md의 `VAULT_ROOT` 값을 실제 볼트 경로로 변경해야 한다.

```bash
# 치환 누락 확인
grep -r "futurewave" ~/.claude/skills/ 2>/dev/null || echo "✅ clean"
```

`✅ clean`이 출력되면 정상.

## 설치

```bash
# 마켓플레이스 등록 (최초 1회)
/plugin marketplace add https://github.com/gihoon/brown-claude-marketplace

# 플러그인 설치
/plugin install greg-skills@greg-claude-marketplace
```

## 플러그인 목록

### greg-skills

아이디어 파이프라인 + 지식관리 파이프라인 + 리포트·발표. 총 11개 스킬.

#### 아이디어 파이프라인

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| `/sharpen` | 모호한 아이디어를 구체적인 명세서로 다듬기 | `/sharpen`, `/구체화` |
| `/productify` | 명세서를 받아 페이즈별 로드맵 설계 | `/productify`, `/제품화` |

#### 지식관리 파이프라인 (Zettelkasten)

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| `/raw` | 임시노트 즉시 저장 / `scan`으로 미처리 목록 확인 | `/raw`, `/raw scan` |
| `/literature` | 문헌노트 생성 (읽은 자료를 자기 말로 소화 → `1 Literature/`) | `/literature` |
| `/perm` | 원자적 영구노트 생성 + VAULT_INDEX 연결 | `/perm` |
| `/wiki` | 클러스터 개념 허브 페이지 생성 | `/wiki` |
| `/index` | 프론트매터 기반 VAULT_INDEX 자동 생성·갱신 | `/index` |
| `/query` | 볼트 4-Way 검색 | `/query` |
| `/lint` | 볼트 건강 점검 | `/lint` |

#### 리포트·발표

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| `/report-design` | DSRV 스타일 기관 리서치 리포트를 A4 PDF로 생성 | `/report-design`, `리포트`, `보고서` |
| `/report-pt` | `agent_payments_PT` 형식의 에디토리얼 슬라이드 덱(HTML) 생성 | `/report-pt`, `발표자료`, `슬라이드` |

#### 파이프라인의 흐름

```
아이디어 떠오름
  │
  ├─ 메모로 남기기 ──→ /raw → /literature → /perm → /wiki   (지식 축적)
  │                                  └→ /index /query /lint  (탐색·점검)
  │
  ├─ 제품으로 만들기 ─→ /sharpen → /productify              (실행 계획)
  │
  └─ 발표·리포트로 ────→ /report-pt · /report-design         (슬라이드 · PDF)
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

### /literature — 읽은 자료를 문헌노트로

책·논문·아티클을 자기 말로 소화해 `1 Literature/`에 기록한다. `/raw`(내 생각)와 달리 **출처가 있는 자료**를 다룬다.

```
/literature 루만 「Communicating with Slip Boxes」 — 제텔카스텐의 핵심은 대화 상대로서의 메모다
```

출처를 체계적으로 남기고, 영구노트로 발전시킬 후보 개념을 표시해준다. → `/perm`으로 이어짐.

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

### /index — VAULT_INDEX 자동 생성·갱신

`2 Permanent/`·`1 Literature/`의 모든 노트 프론트매터(claim·tags·links)를 한 파일로 압축한다. `/perm`·`/query`·`/lint`가 이 인덱스를 읽어 동작하므로, **지식관리 파이프라인의 토대**다.

```
/index
```

RAG 없이 프론트매터만으로 볼트 전체를 탐색 가능하게 만든다. 노트가 추가·수정되면 다시 돌려 갱신한다.

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

### /report-design — 기관급 리서치 리포트 PDF

정리된 내용을 **DSRV 하우스 스타일의 A4 PDF 리포트**로 내보낸다 (JP Morgan·미래에셋 급 기관 리서치 수준). 리포트·보고서·참관/현장 리포트를 요청하면 동작한다.

```
/report-design ETHConf 2026 참관 리포트 만들어줘
```

표지·목차·Executive Summary·"DSRV View" 박스·비교표·풀인용·디스클레이머로 구성되며, Pretendard(한글)+Source Serif 4/Inter(영문) 폰트를 로컬 임베드해 **Chrome headless로 PDF 렌더**한다.

---

### /report-pt — 발표용 슬라이드 덱

정리된 전략·기획을 **에디토리얼 HTML 슬라이드 덱**으로 만든다 (`agent_payments_PT.html` 형식). 스크롤·방향키로 넘기는 풀뷰포트 프레젠테이션.

```
/report-pt 둘레값 사업 피치덱 만들어줘
```

종이 질감·Pretendard·우측 progress dots의 일관된 포맷으로 cover·cards3·timeline·compare·revenue·end 등 슬라이드 타입을 조합한다. `<주제>_PT.html`로 저장 후 브라우저로 발표(필요 시 PDF 인쇄).

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
