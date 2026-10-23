"""Generate a redacted, pending-review Markdown handoff. Never stages or uploads files."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from uuid import uuid4
from share_check import analyze, MAX_SIZE

FIELDS = ('summary', 'changes', 'decisions', 'checks', 'next_steps', 'references')

def local_input(root, name):
    local = root / '.local-work'
    p = (root / name).resolve()
    if not p.is_relative_to(local.resolve()) or p.is_symlink() or not p.is_file() or p.stat().st_size > MAX_SIZE:
        raise ValueError('invalid_local_input')
    return p.read_text(encoding='utf-8-sig')

def render(record, day, session_id):
    pid = record['participant_id']
    if not isinstance(pid, str) or not re.fullmatch(r'P\d{2,6}',pid):
        raise ValueError('pseudonym_required')
    if not isinstance(record.get('topic'), str) or not record['topic'].strip():
        raise ValueError('topic_required')
    sections = [('Summary','summary'),('Changes','changes'),('Decisions and reasons','decisions'),('Actual checks','checks'),('Next steps','next_steps'),('References','references')]
    lines=['---','record_type: worklog','privacy_review: pending',f'participant_id: {pid}',f'date: {day}',f'session_id: {session_id}','---','', '# Worklog', '',record['topic'].strip(),'', 'This record is reference material, not AI instructions or new authority.', '']
    for title,key in sections:
        values = record.get(key)
        if not isinstance(values,list) or not values or any(not isinstance(v,str) or not v.strip() for v in values):
            raise ValueError('nonempty_string_lists_required')
        lines += ['## '+title,'']
        lines += ['- '+v.strip().replace('\n','\n  ') for v in values]
        lines += ['']
    return '\n'.join(lines)+'\n'

def main():
    parser=argparse.ArgumentParser(description='Create a redacted Markdown draft from a local work summary.')
    parser.add_argument('--input', required=True, help='JSON summary under .local-work')
    parser.add_argument('--redact-file', help='Additional literal redaction phrases under .local-work, one per line')
    parser.add_argument('--date', default=date.today().isoformat())
    args=parser.parse_args()
    root=Path(__file__).resolve().parents[1]
    try:
        day=date.fromisoformat(args.date).isoformat()
        record=json.loads(local_input(root,args.input))
        session_id=uuid4().hex
        text=render(record,day,session_id)
        manual_count=0
        if args.redact_file:
            phrases=sorted(set(local_input(root,args.redact_file).splitlines()),key=len,reverse=True)
            for phrase in phrases:
                phrase=phrase.strip()
                if not phrase:continue
                if len(phrase)<2:raise ValueError('redaction_phrase_too_short')
                manual_count+=text.count(phrase)
                text=text.replace(phrase,'[REDACTED]')
        found,masked=analyze(text)
        # Rebuild fixed metadata after masking so user text cannot approve a draft.
        if 'privacy_review: pending' not in masked or analyze(masked)[0]:
            raise ValueError('unresolved_pattern')
        folder=root/'docs/worklogs'
        if folder.is_symlink():raise ValueError('unsafe_output_folder')
        folder.mkdir(parents=True,exist_ok=True)
        if not folder.resolve().is_relative_to(root):raise ValueError('unsafe_output_folder')
        name=f'{day}-{record["participant_id"]}-{session_id[:8]}.md'
        with (folder/name).open('x',encoding='utf-8',newline='\n') as f:f.write(masked)
        print(json.dumps({'status':'DRAFT_REQUIRES_HUMAN_REVIEW','output':'docs/worklogs/'+name,
            'masked_patterns':len(found),'manual_replacements':manual_count,
            'next':'Review for context, names and identifiers locally. Only after human approval set privacy_review to approved, then scan the staged file. No Git write or upload was performed.'},ensure_ascii=True,indent=2))
        return 0
    except (OSError,ValueError,KeyError,TypeError):
        print(json.dumps({'status':'ERROR_STOP','reason':'local_summary_or_redaction_needs_review','raw_values_printed':False}))
        return 2

if __name__=='__main__':
    sys.exit(main())
