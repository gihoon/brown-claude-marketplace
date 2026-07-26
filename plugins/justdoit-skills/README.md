# justdoit-skills

지식관리 파이프라인과 아이디어 파이프라인을 하나로 묶은 Claude Code 스킬 패키지.

> **출처**
> - 원본 저장소: [kimyoon21/brown-claude-marketplace](https://github.com/kimyoon21/brown-claude-marketplace)
> - 참고 자료: [vibelabs.kr/shared/8](https://vibelabs.kr/shared/8)

## 스킬 목록

### 지식관리 파이프라인 (Zettelkasten)

```
/doit-raw → /doit-literature → /doit-perm → /doit-wiki
                        ↓
              /doit-index  /doit-query  /doit-lint
```

| 스킬 | 설명 |
|------|------|
| `/doit-raw` | 임시노트 즉시 저장. `/doit-raw scan`으로 미처리 목록 확인 후 영구노트 전환 |
| `/doit-literature` | 문헌노트 생성. 읽은 자료를 자기 말로 소화해 `1 Literature/`에 저장 |
| `/doit-perm` | 원자적 영구노트 생성. VAULT_INDEX 연결 + cascade.py 후처리 |
| `/doit-wiki` | 클러스터 개념 허브 페이지 생성 |
| `/doit-index` | 프론트매터 기반 VAULT_INDEX 자동 생성·갱신 (perm·query·lint의 토대) |
| `/doit-query` | 볼트 4-Way 검색 (키워드·태그·클러스터·연결 기준) |
| `/doit-lint` | 볼트 건강 점검 (고아 노트, 깨진 링크, 미처리 raw) |

### 아이디어 파이프라인

```
/doit-sharpen → /doit-productify
```

| 스킬 | 설명 |
|------|------|
| `/doit-sharpen` | 모호한 아이디어·요청을 구체적인 명세서로 다듬기 |
| `/doit-productify` | 명세서를 받아 최적 제품 형태 결정 + 페이즈별 로드맵 설계 |

### 리포트·발표

| 스킬 | 설명 |
|------|------|
| `/doit-report` | 기관 리서치 리포트를 A4 PDF로 생성 (Chrome headless 렌더) |
| `/doit-pt` | 에디토리얼 슬라이드 덱(HTML) 생성 |

### 검증·자동화

| 스킬 | 설명 |
|------|------|
| `/doit-critique` | 명세·기획 노트 적대적 검증 — 미검증 가정·경쟁 누락·논리 구멍 탐지 |
| `/doit-ingest` | PDF·URL·이미지를 문헌노트로 일괄 인제스트 |
| `/doit-relink` | frontmatter links[] 기반 양방향 링크·VAULT_INDEX 재정합 |
| `/doit-refactor` | 노트 이동·ID 재배치·병합·분할 시 링크 정합 유지 |
| `/doit-breakdown` | 큰 노트를 원자적 하위 영구노트들로 분해 |
| `/doit-compile` | 볼트 노트들을 슬라이드·리포트로 컴파일 |
| `/doit-research` | 웹 검색으로 시장·경쟁·기술 근거 수집·보강 |
| `/doit-decide` | 제품·아키텍처 결정을 ADR 형식으로 기록 |

## 사용 예시

```
/doit-raw 오늘 미팅에서 나온 아이디어 메모
/doit-perm 새로운 인사이트 정리
/doit-query 지식관리 관련 노트 찾아줘
/doit-sharpen 이 아이디어를 제품 명세로 만들어줘
/doit-critique ./spec.md
/doit-productify
/doit-compile pt AI에이전트
```
