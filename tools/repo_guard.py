"""Check Git index blobs, not working-tree copies. Local only; no raw content logs."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import PurePosixPath
from share_check import analyze, MAX_SIZE, TEXT_SUFFIXES

REQUIRED = ('AGENTS.md', 'SECURITY.md', 'tools/repo_guard.py', 'tools/share_check.py')

def reviewed_worklog(text):
    header = re.match(r'\A---\n(.*?)\n---(?:\n|\Z)',text.replace('\r\n','\n'),re.S)
    if not header:return False
    metadata = {}
    for line in header.group(1).splitlines():
        if ':' not in line:return False
        key,value=line.split(':',1)
        if key in metadata:return False
        metadata[key]=value.strip()
    return metadata.get('record_type')=='worklog' and metadata.get('privacy_review')=='approved' and bool(re.fullmatch(r'P\d{2,6}',metadata.get('participant_id','')))

def git(*args):
    result = subprocess.run(['git', *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise ValueError('git_operation_failed')
    return result.stdout

def main():
    parser = argparse.ArgumentParser(description='Check actual commit candidates in the Git index.')
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--staged', action='store_true', help='Check changed index entries only')
    mode.add_argument('--tracked', action='store_true', help='Check all tracked entries in the current index')
    args = parser.parse_args()
    findings = []
    try:
        entries = {}
        for row in git('ls-files', '--stage', '-z').split(b'\0'):
            if not row:
                continue
            metadata, raw_path = row.split(b'\t', 1)
            mode_value, oid, stage = metadata.decode('ascii').split()
            if stage != '0':
                raise ValueError('unmerged_index')
            entries[raw_path.decode('utf-8')] = (mode_value, oid)
        for name in REQUIRED:
            if name not in entries:
                findings.append({'rule': 'required_policy_or_checker_missing', 'required_file': name})
        changed = {p.decode('utf-8') for p in git('diff', '--cached', '--name-only', '-z', '--diff-filter=ACMR').split(b'\0') if p}
        selected = sorted(entries if args.tracked else changed)
        for number, name in enumerate(selected, 1):
            mode_value, oid = entries[name]
            path = PurePosixPath(name)
            if any(part in {'.local-work', '.private'} for part in path.parts):
                findings.append({'file_number': number, 'rule': 'local_raw_record_not_shareable', 'action': 'STOP'})
                continue
            if path.name == '.env' or path.name.startswith('.env.') and path.name != '.env.example' or path.suffix.lower() in {'.pem', '.key', '.p12', '.pfx', '.keystore'}:
                findings.append({'file_number': number, 'rule': 'sensitive_filename', 'action': 'STOP'})
                continue
            allowed = path.suffix.lower() in TEXT_SUFFIXES or path.name in {'.gitignore', '.env.example'}
            if mode_value not in {'100644', '100755'} or not allowed:
                findings.append({'file_number': number, 'rule': 'unsupported_file_manual_review_required', 'action': 'STOP'})
                continue
            if int(git('cat-file', '-s', oid)) > MAX_SIZE:
                findings.append({'file_number': number, 'rule': 'file_too_large_manual_review_required', 'action': 'STOP'})
                continue
            raw = git('cat-file', 'blob', oid)
            if b'\x00' in raw:
                findings.append({'file_number': number, 'rule': 'binary_file_manual_review_required', 'action': 'STOP'})
                continue
            try:
                text = raw.decode('utf-8-sig')
            except UnicodeError:
                findings.append({'file_number': number, 'rule': 'encoding_manual_review_required', 'action': 'STOP'})
                continue
            detected, _ = analyze(text)
            if path.parts[:2] == ('docs', 'worklogs') and path.name != 'README.md':
                if not reviewed_worklog(text):
                    findings.append({'file_number': number, 'rule': 'worklog_human_review_required', 'action': 'STOP'})
            for item in detected:
                findings.append({'file_number': number, **item, 'action': 'STOP'})
        print(json.dumps({'decision': 'STOP' if findings else 'NO_PATTERN_FOUND',
            'scope': 'tracked_index' if args.tracked else 'changed_index', 'files_checked': len(selected),
            'findings': findings, 'notice': 'No source values printed. No pattern found is not proof of safety.'}, ensure_ascii=False, indent=2))
        return 2 if findings else 0
    except (OSError, ValueError, KeyError, UnicodeError):
        print(json.dumps({'decision': 'ERROR_STOP', 'rule': 'index_could_not_be_verified'}))
        return 3

if __name__ == '__main__':
    sys.exit(main())
