"""Install an opt-in pre-commit hook without replacing existing hooks or config."""
from pathlib import Path
import shlex
import subprocess
import sys

def git(*args):
    return subprocess.run(['git', *args], capture_output=True, text=True)

def main():
    root = git('rev-parse', '--show-toplevel')
    if root.returncode:
        print('STOP: Git 저장소 루트에서 실행하세요.')
        return 2
    configured = git('config', '--get', 'core.hooksPath')
    if configured.returncode == 0:
        print('STOP: 기존 core.hooksPath가 있습니다. 팀 관리자와 기존 훅에 검사를 통합하세요.')
        return 2
    hook_path = git('rev-parse', '--git-path', 'hooks/pre-commit')
    if hook_path.returncode:
        print('STOP: 훅 위치를 확인할 수 없습니다.')
        return 2
    hook = Path(hook_path.stdout.strip())
    if hook.exists() or hook.is_symlink():
        print('STOP: 기존 pre-commit 훅을 덮어쓰지 않았습니다.')
        return 2
    checker = Path(root.stdout.strip()) / 'tools/repo_guard.py'
    if not checker.is_file():
        print('STOP: tools/repo_guard.py가 없습니다.')
        return 2
    hook.parent.mkdir(parents=True, exist_ok=True)
    executable = shlex.quote(sys.executable.replace('\\', '/'))
    hook.write_text('#!/bin/sh\nexec ' + executable + ' tools/repo_guard.py --staged\n', encoding='utf-8', newline='\n')
    hook.chmod(hook.stat().st_mode | 0o111)
    print('설치 완료: 이 로컬 저장소의 커밋 직전에 index를 검사합니다. 다른 복제본에는 각각 설치해야 합니다.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
