"""Build/audit the criterion matrix from the SRS, named cases and recorded run."""
import argparse
import ast
import csv
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ('requirement_id', 'priority', 'criterion_id', 'test_case_id', 'level', 'status',
          'defect_id', 'criterion', 'note')
ACCEPTANCE = 'tests/acceptance/test_m11_criteria.py'
EXISTING = 'tests/test_iteration1.py'
EXISTING_CASES = {
    'FR-ACCT-03-AC1': 'test_password_change_ac1_persists_hash_revokes_all_sessions_and_reauthenticates',
    'FR-ACCT-03-AC2': 'test_password_change_ac2_invalid_password_never_overwrites',
    'FR-CHAT-04-AC1': 'test_chat_ac1_ac2_ac5_persists_username_time_and_is_visible_to_members',
    'FR-CHAT-04-AC2': 'test_chat_ac1_ac2_ac5_persists_username_time_and_is_visible_to_members',
    'FR-CHAT-04-AC5': 'test_chat_ac1_ac2_ac5_persists_username_time_and_is_visible_to_members',
    'FR-CLNDR-03-AC1': 'test_delete_event_ac1_ac2_selection_confirmation_and_persistence',
    'FR-CLNDR-03-AC2': 'test_delete_event_ac1_ac2_selection_confirmation_and_persistence',
    'FR-CLNDR-03-AC3': 'test_delete_event_ac3_exact_invalid_event_error',
    'FR-CLNDR-03-AC4': 'test_delete_event_ac4_ac5_cross_unit_member_and_csrf_denied',
    'FR-CLNDR-03-AC5': 'test_delete_event_ac4_ac5_cross_unit_member_and_csrf_denied',
}


def requirements():
    srs = (ROOT/'docs/requirements.md').read_text(encoding='utf-8')
    for rid, body in re.findall(r'^### (FR-[\w-]+) [^\n]+\n(.*?)(?=^#{2,3} |\Z)', srs, re.M | re.S):
        priority = re.search(r'\*\*Priority:\*\* (\w+)', body)[1]
        criteria = body.split('**Acceptance criteria:**', 1)[1].split('**Source:**', 1)[0]
        values = [line.strip()[2:].lstrip('* ').strip() for line in criteria.splitlines() if line.strip().startswith('- ')]
        assert values, rid
        yield rid, priority, values
    for line in srs.splitlines():
        if line.startswith('| NFR-'):
            rid, priority, *values = [v.strip() for v in line.strip('|').split('|')]
            yield rid, priority, [' | '.join(values)]


def rows():
    source = ast.parse((ROOT/ACCEPTANCE).read_text(encoding='utf-8'))
    catalog = {node.targets[0].id: ast.literal_eval(node.value) for node in source.body
               if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
               and node.targets[0].id in ('KNOWN', 'FIXED', 'CASES')}
    observed = json.loads((ROOT/'docs/milestone-11-run.json').read_text(encoding='utf-8'))['cases']
    for rid, priority, criteria in requirements():
        for i, criterion in enumerate(criteria, 1):
            cid = f'{rid}-AC{i}'
            test, level, status, defect, note = '', '', 'gap', '', 'No verified case for this criterion.'
            if cid in catalog['CASES']:
                test = f'{ACCEPTANCE}::test_written_criterion[{cid}]'
                level = 'acceptance'
                defect = catalog['KNOWN'].get(cid, catalog['FIXED'].get(cid, ''))
                outcome = observed.get('test_written_criterion['+cid+']')
                status = 'failed' if outcome == 'xfail' else 'passed' if outcome == 'passed' else 'not-run'
                note = ('Known defect reproduced; strict expected failure.' if cid in catalog['KNOWN'] else
                        'Regression passed after baseline failure.' if defect else 'Controlled HTTP acceptance.')
            elif cid in EXISTING_CASES:
                name = EXISTING_CASES[cid]
                test, level = EXISTING+'::'+name, 'acceptance'
                matches = [state for key, state in observed.items() if key == name or key.startswith(name+'[')]
                status = 'passed' if matches and all(state == 'passed' for state in matches) else 'not-run'
                note = 'Retained Week 10 regression evidence, rerun this week.'
            elif rid == 'NFR-SEC-02':
                name = 'test_nfr_sec_02_every_post_missing_or_modified_csrf'
                test, level = ACCEPTANCE+'::'+name, 'acceptance'
                status = 'passed' if observed.get(name) == 'passed' else 'not-run'
                note = 'Enumerates every registered POST route and checks no database mutation.'
            elif rid.startswith('NFR-') and priority == 'Must':
                test, level, status = f'docs/milestone-11-manual-cases.md::{cid}', 'manual acceptance', 'not-run'
                note = 'Procedure available; required observation pending.'
            if status == 'passed' and rid in {'FR-CHAT-04', 'FR-CHAT-05'}:
                status, note = 'partial', 'Unit-wide chat exercised; distinct selectable group chat is absent.'
            if rid == 'FR-RANK-05' and status == 'passed':
                status, note = 'partial', 'One prohibited administrative action checked; full hierarchy absent.'
            if rid == 'FR-CLNDR-02' and status == 'passed':
                status, note = 'partial', 'Unit events verified; separately created calendar prerequisite absent.'
            yield dict(zip(FIELDS, (rid, priority, cid, test, level, status, defect, criterion, note)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    matrix = ROOT/'docs/traceability.csv'
    expected = list(rows())
    assert len({row['criterion_id'] for row in expected}) == len(expected)
    assert len({row['requirement_id'] for row in expected}) == 43
    must = {r['requirement_id'] for r in expected if r['priority'] == 'Must'}
    mapped = {r['requirement_id'] for r in expected if r['test_case_id']}
    assert must <= mapped, sorted(must-mapped)
    if args.check:
        with matrix.open(newline='', encoding='utf-8') as handle:
            assert list(csv.DictReader(handle)) == expected, 'Matrix differs from SRS or recorded run'
    else:
        with matrix.open('w', newline='', encoding='utf-8') as handle:
            out = csv.DictWriter(handle, FIELDS, lineterminator='\n')
            out.writeheader()
            out.writerows(expected)
    print(f'{len(expected)} criteria; {len(must)}/{len(must)} Must requirements have a case.')


if __name__ == '__main__':
    main()
