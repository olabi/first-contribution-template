# Windows와 macOS 설치와 첫 실행

이 문서는 공개 템플릿에서 팀의 비공개 프로젝트를 시작하는 순서입니다. 템플릿은 공개여도 새로 만드는 프로젝트는 비공개로 선택할 수 있습니다.

## 먼저 비공개 저장소 만들기

1. 공개 템플릿의 Use this template에서 Create a new repository를 선택합니다.
2. 소유자와 프로젝트 이름을 정하고 Visibility를 Private으로 선택해 생성합니다.
3. 저장소 이름 옆에 Private 표시가 있는지 확인한 뒤 팀원을 초대합니다.
4. 생성한 비공개 저장소를 복제합니다. 공개 템플릿 저장소를 작업 대상으로 쓰지 마세요.

공개 저장소의 Fork 버튼으로 만든 포크는 공개이며 독립적으로 비공개 전환할 수 없습니다. 팀 프로젝트 시작에는 템플릿 복사를 사용합니다. 템플릿 복사에는 원본 이슈·권한·Secrets·Linear 연결·로컬 훅 설정이 자동 복사되지 않습니다.

공식 안내: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template

## 필요한 것과 선택할 것

- Codex를 사용할 수 있는 데스크톱 앱과 학교 계정: AI 작업 안내에 사용합니다. 학교 정책에 따른 사용 가능 여부를 먼저 확인합니다.
- Git 명령줄: 변경 기록과 커밋 후보 검사를 위해 필요합니다.
- Python 3.10 이상: 이 예제의 분석·공유 전 검사·기여도 계산에 필요합니다. 별도 pip 패키지와 API 키는 필요하지 않습니다.
- GitHub 계정과 비공개 저장소 초대: 원격 공동 작업에 필요합니다.
- Linear 계정과 팀 초대: Linear 연습을 할 때 필요합니다. 브라우저로 사용할 수 있어 앱 설치는 필수가 아닙니다.
- GitHub Desktop: 선택 사항입니다. 버튼으로 복제·변경 비교·PR을 진행할 때 편리합니다. 이 키트의 검사는 터미널에서 git 명령이 별도로 실행되어야 합니다.
- VS Code·Node.js·Homebrew·GitHub CLI: 이 키트의 필수 도구가 아닙니다. 프로젝트가 필요로 할 때 추가합니다.

## Windows

1. Git 공식 페이지 https://git-scm.com/install/windows 에서 CPU에 맞는 x64 또는 ARM64 설치 파일을 사용합니다. Windows 설정의 시스템 정보에서 시스템 종류를 확인합니다. 명령줄과 다른 앱에서 Git을 사용할 수 있는 설치 옵션을 선택합니다.
2. Python 공식 페이지 https://www.python.org/downloads/windows/ 에서 지원 중인 안정 버전과 CPU에 맞는 설치 방식을 선택합니다. 설치 프로그램에 PATH 추가 옵션이 있다면 활성화합니다. 임베더용 패키지는 입문 설치용이 아닙니다.
3. 설치 후 PowerShell과 Codex를 다시 열고 아래 명령을 실행합니다. Python 실행기 py가 없다면 python --version으로 확인한 후 python 명령으로 대체합니다.

```powershell
git --version
py -3 --version
```

4. GitHub Desktop을 사용할 경우 https://desktop.github.com/download/ 에서 Windows용을 설치하고 브라우저 인증으로 로그인합니다. 팀의 비공개 저장소를 복제하고 해당 폴더를 Codex 로컬 프로젝트로 엽니다.
5. 복제한 저장소 루트의 PowerShell에서 실행합니다.

```powershell
py -3 tools/install_guard_hook.py
py -3 scripts/analyze.py
py -3 tools/contribution_score.py
```

git 명령을 찾지 못하면 Git 설치의 PATH 설정과 새 터미널 여부를 확인합니다. python 명령이 스토어만 열면 py -3 또는 공식 설치의 실행 경로를 확인합니다. 학교 관리 PC에서 설치가 막히면 관리자에게 요청합니다.

## macOS

1. 터미널에서 git --version을 실행합니다. 설치되어 있지 않으면 아래 명령으로 Apple Command Line Tools를 설치하고 다시 확인합니다. 이미 Homebrew를 사용하는 사람은 Git 공식 안내의 brew install git 방식도 선택할 수 있습니다.

```sh
xcode-select --install
git --version
```

2. https://www.python.org/downloads/macos/ 에서 지원되는 안정 버전의 macOS 설치 프로그램을 사용합니다. 자신의 macOS 버전 지원 여부를 설치 페이지에서 확인합니다. 설치 후 새 터미널에서 확인합니다.

```sh
python3 --version
```

3. 선택 도구인 GitHub Desktop은 https://desktop.github.com/download/ 에서 Apple Silicon 또는 Intel Mac에 맞게 선택합니다. Apple 메뉴의 이 Mac에 관하여에서 칩을 확인합니다.
4. 팀의 비공개 저장소를 복제하고 해당 폴더를 Codex에서 연 뒤 터미널에서 실행합니다.

```sh
python3 tools/install_guard_hook.py
python3 scripts/analyze.py
python3 tools/contribution_score.py
```

## Git 작성자와 첫 작업

Git 작성자 이름과 이메일은 커밋에 기록됩니다. 저장소 루트에서 팀이 사용할 표시 이름과 GitHub 설정에서 확인한 noreply 이메일을 지정합니다. 아래 대괄호 부분은 자신의 값으로 바꿉니다. 이메일을 채팅에 제출할 필요는 없습니다.

```sh
git config user.name "[표시 이름]"
git config user.email "[GitHub에서 확인한 noreply 주소]"
git status
git remote -v
```

remote가 팀의 비공개 저장소를 가리키는지 확인하고, 연결에 문제가 있으면 공개 전환으로 해결하지 않습니다. GitHub 로그인은 브라우저 인증을 사용하고 토큰을 명령·문서에 붙이지 않습니다.

## 준비 완료 확인

분석 예제의 출력은 rows=6, mean_study_hours=3.50, mean_quiz_score=75.00입니다. 기여도 예제는 팀 승인 완료점수 80점이며 P01 25점, P02 35점, P03 20점입니다. 모두 가상 자료입니다.

AGENTS.md와 SECURITY.md를 읽은 후 작은 문서 작업을 시작합니다. 필요한 파일만 git add로 추가한 뒤 Windows는 py -3 tools/repo_guard.py --staged, macOS는 python3 tools/repo_guard.py --staged로 점검합니다. 훅은 복제본마다 설치해야 합니다. 훅·검사 코드·CI 변경도 팀 검토 대상입니다.

실습 도구는 Windows에서 검증했으며 macOS 설치·실행 안내는 공식 문서 기준입니다. 실제 macOS 기기에서의 실행은 별도로 확인해야 합니다. 버전 번호는 고정하지 않고 공식 페이지의 지원되는 안정 버전을 사용합니다. 확인일 2026년 10월 23일.
