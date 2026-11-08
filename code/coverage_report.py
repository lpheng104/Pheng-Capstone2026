"""Calculate verified-requirement coverage from the Milestone 11 criterion matrix."""
import argparse
from collections import defaultdict
import csv


def calculate(path):
    requirements = defaultdict(list)
    with open(path, newline='', encoding='utf-8') as handle:
        for row in csv.DictReader(handle):
            requirements[row['requirement_id']].append(row)
    verified = {rid for rid, rows in requirements.items() if all(r['status'] == 'passed' for r in rows)}
    must = {rid for rid, rows in requirements.items() if rows[0]['priority'] == 'Must'}
    return len(requirements), len(verified), len(must), len(verified & must)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('matrix', nargs='?', default='docs/traceability.csv')
    args = parser.parse_args()
    total, verified, must, verified_must = calculate(args.matrix)
    print(f'Total requirements: {total}')
    print(f'Verified requirements: {verified}')
    print(f'Verified-requirement coverage: {verified}/{total} ({verified/total:.1%})')
    print(f'Verified-Must coverage: {verified_must}/{must} ({verified_must/must:.1%})')
