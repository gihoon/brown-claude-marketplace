# brown-claude-marketplace

Claude Code 플러그인 모음. 아이디어를 실제 제품으로 만드는 데 도움을 주는
스킬들을 공개 마켓플레이스 형태로 관리합니다.

## 요구사항

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- Claude Pro 이상 (Agent 서브에이전트 사용)

## 설치

```bash
# 마켓플레이스 등록 (최초 1회)
/plugin marketplace add https://github.com/kimyoon21/brown-claude-marketplace

# 플러그인 설치
/plugin install productify@brown-claude-marketplace
```

## 플러그인 목록

### productify

아이디어나 명세서를 받아 **최적의 제품 형태**를 결정하고
**페이즈별 로드맵**을 설계하는 스킬.

경량화 우선 원칙으로 가장 작은 리소스로 문제를 해결할 수 있는
형태(Claude 스킬 / 스크립트 / 크롬 익스텐션 / 로컬 HTML / 서비스 등)를
자동으로 찾아줍니다.

**트리거**: "productify", "제품화", "어떻게 만들지", "로드맵 짜줘",
"뭐부터 만들지", "MVP 플래닝", "페이즈 나눠줘"

**지원 입력**:

- 텍스트로 아이디어 설명
- 로컬 명세서 파일 경로
- Notion 페이지 URL
- Google Docs / Sheets URL

**결과물 저장**: 로컬 파일, Notion 페이지, Slack 메시지 전송 가능

## 업데이트

```bash
/plugin update productify@brown-claude-marketplace
```
