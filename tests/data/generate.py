"""Generate deterministic fictional fixture input; no service connections."""
import argparse
import json
from pathlib import Path
import random


def families():
    rng = random.Random(1108)
    suffix = rng.randrange(10000, 99999)
    return {
        'happy': {'unit': f'Fictional Squad {suffix}', 'message': 'Practice at the demo field.',
                  'event': {'title': 'Fictional briefing', 'starts_at': '2030-01-02T06:00:00-06:00',
                            'location': 'Demo field'}},
        'boundary': {'passwords': ['Aa!1234', 'Aa!12345', 'Aa!'+'x'*125, 'Aa!'+'x'*126],
                     'message_lengths': [0, 1, 1999, 2000, 2001],
                     'dates': ['2030-02-29T12:00:00+00:00', '2032-02-29T12:00:00+00:00',
                               '2030-01-02T12:00:00', '']},
        'hostile': {'markup': '<script>alert(1)</script>', 'spaces': '   ',
                    'invalid_id': 'not-an-object-id', 'unknown_user': f'fictional_missing_{suffix}'},
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for family, values in families().items():
        path = Path(__file__).with_name(family + '.json')
        content = json.dumps(values, indent=2, sort_keys=True) + '\n'
        if args.check:
            assert path.read_text(encoding='utf-8') == content, path.name
        else:
            path.write_text(content, encoding='utf-8')
