"""C1: convert service results into the server-rendered unit page."""
from flask import render_template

from src.messaging import latest_messages
from src.scheduling import event_roster
from src.unit_access import roster


def render_unit(store, unit_id, user_id):
    unit, member, members = roster(store, unit_id, user_id)
    return render_template('unit.html', unit=unit, member=member, members=members,
                           messages=latest_messages(store, unit_id, user_id),
                           events=event_roster(store, unit_id, user_id))
