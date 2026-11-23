"""Static Milestone 13 document checks; not command execution or human evidence."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
NAMES=['README.md','docs/runbook.md','docs/onboarding.md','docs/adr/README.md',
       'docs/adr/0005-admin-bootstrap-boundary.md','docs/clean-machine-test.md',
       'docs/clean-machine-format-example.md','docs/command-verification.md']


def check():
    errors=[]
    readme=(ROOT/'README.md').read_text(encoding='utf-8')
    headings=re.findall(r'^## (\d+)\.',readme,re.M)
    if headings != [str(i) for i in range(1,12)]:
        errors.append('README must contain the eleven numbered sections in order')
    for name in NAMES:
        text=(ROOT/name).read_text(encoding='utf-8')
        if not text.startswith('# '):
            errors.append(name+': missing title')
        for target in re.findall(r'(?<!!)\[[^\]]+\]\(([^)]+)\)',text):
            target=target.strip('<>')
            parsed=urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            path=((ROOT/name).parent/unquote(parsed.path)).resolve()
            if not path.is_relative_to(ROOT.resolve()) or not path.exists():
                errors.append(name+': missing local link '+target)
    arch=(ROOT/'docs/architecture.md').read_text(encoding='utf-8')
    for section in ('## 0 — Overview (as built)','## 1. Purpose and Scope','## 2. System Context'):
        if section not in arch:
            errors.append('architecture missing retained/added section: '+section)
    print('Static documentation errors:',len(errors))
    for error in errors:
        print(error)
    print('This checks structure and selected links only; personal commands and human test are not verified.')
    return bool(errors)


if __name__=='__main__':
    sys.exit(check())
