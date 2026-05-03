# brown-claude-marketplace

Claude Code 플러그인 모음. 아이디어를 실제 제품으로 만드는 데 도움을 주는
스킬들을 공개 마켓플레이스 형태로 관리합니다.

> **Claude + Notion + Slack을 주로 사용하는 조직에 최적화**되어 있습니다.
> 다른 환경을 쓰는 경우, 스킬을 포크하거나 `allowed-tools`를 수정해서
> 그대로 가져다 쓰면 됩니다.

## 요구사항

- [Claude Code](https://claude.ai/code) (CLI 또는 데스크탑 앱)
- Claude Pro 이상 (Agent 서브에이전트 사용)

## 설치

```bash
# 마켓플레이스 등록 (최초 1회)
/plugin marketplace add https://github.com/kimyoon21/brown-claude-marketplace

# 플러그인 설치
/plugin install ideas-come-true@brown-claude-marketplace
```

## 플러그인 목록

### ideas-come-true

아이디어를 실제 제품으로 만드는 스킬 모음.
**sharpen → productify** 순서로 사용하면 아이디어에서 로드맵까지 한 번에 완성됩니다.

| 스킬 | 설명 | 트리거 |
|------|------|--------|
| sharpen | 모호한 아이디어·요청을 구체적인 명세서로 다듬기 | "sharpen", "구체화해줘", "명세 잡아줘" 등 |
| productify | 명세서를 받아 최적 제품 형태 결정 + 페이즈별 로드맵 설계 | "productify", "제품화", "로드맵 짜줘" 등 |

**productify 지원 입력**:

- 텍스트로 아이디어 설명
- 로컬 명세서 파일 경로
- Notion 페이지 URL
- Google Docs / Sheets URL

**결과물 저장**: 로컬 파일 또는 Notion 페이지

## 업데이트

```bash
/plugin update ideas-come-true@brown-claude-marketplace
```
