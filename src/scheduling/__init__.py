"""C5: assemble upcoming events and attendance intentions for current members."""
from src.unit_access import roster


def event_roster(store, unit_id, user_id):
    unit, _, members = roster(store, unit_id, user_id)
    events = store.many('events', {'unit_id': unit['_id']},
                        [('starts_at', 1), ('_id', 1)])
    for event in events:
        responses = {str(row['user_id']): row['status'] for row in
                     store.many('responses', {'event_id': event['_id']})}
        event['mine'] = responses.get(str(user_id), 'pending')
        event['attendance'] = [
            {'name': member['user']['name'],
             'status': responses.get(str(member['user_id']), 'pending')}
            for member in members
        ]
    return events
