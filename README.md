# productify — Claude Code Plugin

아이디어나 명세서를 받아 **어떤 제품 형태로 만들지** 결정하고 **페이즈별 로드맵**을 설계하는 Claude Code 스킬.

## 무엇을 하나요

- 경량화 우선 원칙 적용 (claude-skill → script → … → web-service 순)
- 팀 서비스 환경 파악 후 후보 형태 필터링
- Form Judge(AI 판정)로 형태 명확성 0-100점 스코어링
- 외부 의존성 전수 평가 + API 키 요청서 자동 생성
- 보안 등급 판정 (🔴 STOP / 🟡 REVIEW / 🟢 SAFE)
- 페이즈별 로드맵 문서 생성 (Notion 또는 로컬 .md)

## 설치

```bash
# 1. 마켓플레이스 추가
/plugin marketplace add https://github.com/kimyoon21/productify

# 2. 플러그인 설치
/plugin install idea-develop@productify
```

## 사용

```
/productify {아이디어 또는 명세서 텍스트 / Notion URL / .md 파일 경로}
```

트리거 키워드: `productify`, `제품화`, `어떻게 만들지`, `로드맵 짜줘`,
`뭐부터 만들지`, `MVP 플래닝`, `페이즈 나눠줘` 등을 언급하면 자동 실행.
