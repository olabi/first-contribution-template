# 첫 기여 협업 시작 템플릿

Codex·Linear·GitHub가 낯선 팀원이 첫 작업을 이해하고 안전하게 기여하도록 돕는 한국어 템플릿입니다. 논문 공동연구, 개발 프로젝트, 팀플과 TF에서 사용할 수 있습니다.

## 비공개 프로젝트로 시작하기

이 공개 저장소에서 **Use this template → Create a new repository → Private**을 선택하세요. 생성 후 Private 표시를 확인하고 팀원을 초대하세요. 공개 Fork를 만든 뒤 비공개로 전환하는 방식은 사용할 수 없습니다.

새 저장소의 이슈·권한·Secrets·Linear 연결과 로컬 훅은 각각 설정해야 합니다. 실제 연구자료·개인정보·키는 공개 템플릿에 올리지 마세요. 템플릿 개선 제안에는 가상 예제만 사용하세요.

## 처음 실행할 순서

1. [Windows와 macOS 설치 안내](docs/local_setup.md)를 따라 Git과 Python 3를 준비합니다. GitHub Desktop은 선택 사항입니다.
2. 새 비공개 저장소를 복제하고 Codex 로컬 프로젝트로 엽니다.
3. AI는 [AGENTS.md](AGENTS.md)와 [SECURITY.md](SECURITY.md)를 확인하고 작업 범위·검사 명령을 설명합니다.
4. Windows는 `py -3 tools/install_guard_hook.py`, macOS는 `python3 tools/install_guard_hook.py`로 이 복제본에 커밋 전 점검을 설치합니다.
5. [Linear 작업 카드](docs/linear_tasks.md)의 작은 작업 하나를 팀 프로젝트에 등록하고 완료 기준을 합의합니다.
6. 문서를 수정하고 커밋 후보 검사를 통과한 뒤 PR로 검토를 요청합니다.
7. [기여도 기준](docs/contribution.md)에 따라 근거 기록을 확인하고 계산합니다.

## 지침과 코드로 이중 확인

- AGENTS.md: 작업 전 맥락·권한·민감정보·완료 보고 지침
- tools/repo_guard.py: 작업 폴더가 아닌 Git index의 실제 커밋 후보 검사
- 로컬 pre-commit 훅: 키·개인정보 패턴, 민감 파일, 필수 지침 누락 시 커밋 중단
- GitHub Actions 예제: PR의 추적 파일 검사. 관리자가 필수 검사와 정책 변경 검토를 별도로 설정

패턴 검사는 모든 개인정보·비밀을 찾지 못합니다. 로컬 훅은 우회 가능하며 PR 검사는 이미 푸시한 정보를 되돌리지 못합니다. CI와 필수 검사 설정은 팀 저장소에서 실제 작동을 확인하세요. Linear·AI 입력의 전송 차단과 상시 감시는 아직 구현하지 않았습니다.

## 가상 분석 예제

실행 명령과 출력 의미를 이 부분에 추가하는 것이 첫 문서 작업입니다. scripts/analyze.py는 data/synthetic.csv의 가상 자료 6행을 읽습니다. 실제 참여자 자료가 아니며 인과관계를 주장하지 않습니다.

## 기여도 계산

Windows: `py -3 tools/contribution_score.py`

macOS: `python3 tools/contribution_score.py`

커밋 수·코드 줄 수 대신 사전 합의한 작업 점수, 공동 기여 비율, 근거와 검토 완료 상태를 사용합니다. 성적·저자 순서·인사 평가를 자동 결정하지 않습니다. 자동 계산은 입력된 기록의 산술이며 근거의 진위를 자동 검증하지 않습니다.

## 공개 범위와 재사용

모든 예제는 가상 자료입니다. 이 템플릿의 코드와 문서는 MIT 라이선스로 재사용할 수 있습니다. 생성한 비공개 프로젝트의 비공개 설정과 접근 권한은 팀이 관리합니다. 실제 연구 내용과 별도 저작물의 권리는 각 프로젝트에서 정합니다.
