"""C5: assemble upcoming events and attendance intentions for current members."""
from collections import defaultdict

from src.unit_access import roster


def event_roster(store, unit_id, user_id, *, authorized_roster=None):
    unit, _, members = authorized_roster or roster(store, unit_id, user_id)
    events = store.many('events', {'unit_id': unit['_id']},
                        [('starts_at', 1), ('_id', 1)])
    # AI-assisted 2026-11-15; batch event response reads (DEF-M12-01).
    by_event = defaultdict(dict)
    if events:
        for row in store.many('responses', {'event_id': {'$in': [event['_id'] for event in events]}}):
            by_event[row['event_id']][str(row['user_id'])] = row['status']
    for event in events:
        responses = by_event[event['_id']]
        event['mine'] = responses.get(str(user_id), 'pending')
        event['attendance'] = [
            {'name': member['user']['name'],
             'status': responses.get(str(member['user_id']), 'pending')}
            for member in members
        ]
    return events
