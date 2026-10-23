"""Local teaching example. Explicit UTF-8 files only; no network or recursive scan."""
import argparse
import json
import re
import sys
from pathlib import Path

RULES = [
    ('demo_secret', 'block', re.compile(r'DEMO_SECRET_[A-Za-z0-9_]+')),
    ('github_token', 'block', re.compile(r'(?<![A-Za-z0-9_])(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})(?![A-Za-z0-9_])')),
    ('api_token_shape', 'block', re.compile(r'(?<![A-Za-z0-9_-])sk-[A-Za-z0-9_-]{20,}(?![A-Za-z0-9_-])')),
    ('bearer_token', 'block', re.compile(r'(?i)\bBearer[ \t]+[A-Za-z0-9._~+/-]{16,}=*')),
    ('url_credential', 'block', re.compile(r'(?i)(?:[?&](?:api[_-]?key|access[_-]?token|token|secret|password)=)[^\s&#"\'<>]+')),
    ('jwt_shape', 'block', re.compile(r'(?<![A-Za-z0-9_-])eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+(?![A-Za-z0-9_-])')),
    ('private_key', 'block', re.compile(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----[\s\S]*?(?:-----END (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\Z)')),
    ('credential_assignment', 'block', re.compile(r'''(?im)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password)\b\s*[:=]\s*["']?(?!\s|\[|<|\$)[A-Za-z0-9_+/=.-]{8,}''')),
    ('email', 'review', re.compile(r'(?<![A-Za-z0-9._%+-])[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}(?![A-Za-z0-9_.+-])')),
    ('kr_mobile', 'review', re.compile(r'(?<!\d)01[016789][- ]?\d{3,4}[- ]?\d{4}(?!\d)')),
    ('student_id_context', 'review', re.compile(r'(?:학번|student[_ ]?id)\s*[:=：]?\s*\d{4}[- ]?\d{5,6}', re.I)),
    ('local_user_path', 'review', re.compile(r'(?:[A-Za-z]:[\\/]Users[\\/][^\\/\s"\'<>]+|/(?:Users|home)/[^/\s"\'<>]+)')),
]
MAX_SIZE = 2 * 1024 * 1024
TEXT_SUFFIXES = {'.txt', '.md', '.csv', '.tsv', '.py', '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg', '.html', '.css', '.js', '.ts', '.tsx', '.jsx', '.sh', '.ps1', '.tex', '.bib', '.r', '.sql', '.log'}

def analyze(text):
    found = []
    spans = []
    for name, level, pattern in RULES:
        for match in pattern.finditer(text):
            found.append({'rule': name, 'severity': level, 'line': text.count('\n', 0, match.start()) + 1})
            spans.append((match.start(), match.end()))
    spans.sort()
    merged = []
    for start, end in spans:
        if merged and start <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
        else:
            merged.append((start, end))
    for start, end in reversed(merged):
        text = text[:start] + '[REDACTED]' + text[end:]
    return found, text

def main():
    parser = argparse.ArgumentParser(description='공유 후보 UTF-8 파일을 로컬에서 점검합니다. 원문 값은 출력하지 않습니다.')
    parser.add_argument('files', nargs='+')
    parser.add_argument('--masked-dir', help='선택 사항: 마스킹한 검토용 사본을 저장할 새 폴더. 원본은 보존합니다.')
    args = parser.parse_args()
    reports, copies = [], []
    failed, blocked, review = False, False, False
    for number, name in enumerate(args.files, 1):
        path = Path(name)
        try:
            allowed = path.suffix.lower() in TEXT_SUFFIXES or path.name == '.gitignore' or path.name == '.env' or path.name.startswith('.env.')
            if not allowed or path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_SIZE:
                raise ValueError('unsupported_file')
            raw = path.read_bytes()
            if b'\x00' in raw:
                raise ValueError('binary_file')
            original = raw.decode('utf-8-sig')
            findings, masked = analyze(original)
            reports.append({'file_number': number, 'findings': findings})
            copies.append((number, masked))
            blocked |= any(f['severity'] == 'block' for f in findings)
            review |= bool(findings)
        except (OSError, UnicodeError, ValueError):
            failed = True
            reports.append({'file_number': number, 'error': 'unreadable_or_unsupported_manual_review_required'})
    if args.masked_dir:
        try:
            dest = Path(args.masked_dir)
            dest.mkdir(parents=True, exist_ok=False)
            for number, masked in copies:
                (dest / ('file_%02d.masked.txt' % number)).write_text(masked, encoding='utf-8')
        except OSError:
            failed = True
            reports.append({'error': 'masked_copy_not_created_use_a_new_directory'})
    decision = 'ERROR_STOP' if failed else 'BLOCK' if blocked else 'REVIEW' if review else 'NO_PATTERN_FOUND'
    print(json.dumps({'decision': decision, 'files': reports,
        'notice': 'Local pattern demo only. No automatic publishing. No pattern found does not establish safety.'}, ensure_ascii=False, indent=2))
    return 3 if failed else 2 if blocked else 1 if review else 0

if __name__ == '__main__':
    sys.exit(main())
