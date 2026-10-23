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
        print('STOP: Run from the Git repository root.')
        return 2
    configured = git('config', '--get', 'core.hooksPath')
    if configured.returncode == 0:
        print('STOP: core.hooksPath is already configured. Ask the team administrator to integrate the check with existing hooks.')
        return 2
    hook_path = git('rev-parse', '--git-path', 'hooks/pre-commit')
    if hook_path.returncode:
        print('STOP: Cannot determine the hook path.')
        return 2
    hook = Path(hook_path.stdout.strip())
    if hook.exists() or hook.is_symlink():
        print('STOP: Existing pre-commit hook preserved.')
        return 2
    checker = Path(root.stdout.strip()) / 'tools/repo_guard.py'
    if not checker.is_file():
        print('STOP: tools/repo_guard.py is missing.')
        return 2
    hook.parent.mkdir(parents=True, exist_ok=True)
    executable = shlex.quote(sys.executable.replace('\\', '/'))
    hook.write_text('#!/bin/sh\nexec ' + executable + ' tools/repo_guard.py --staged\n', encoding='utf-8', newline='\n')
    hook.chmod(hook.stat().st_mode | 0o111)
    print('Installed: checks this clone\'s index before commits. Install separately in every clone.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
