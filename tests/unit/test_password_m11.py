"""Candidate password assertions for FR-ACCT-02 and FR-ACCT-03."""
import pytest

from src.identity import password_valid


@pytest.mark.parametrize('index,valid', [(0, False), (1, True), (2, True), (3, False)])
def test_password_length_partition(fictional_data, index, valid):
    assert bool(password_valid(fictional_data['boundary']['passwords'][index])) is valid


@pytest.mark.parametrize('value,valid', [
    ('AA!12345', False), ('aa!12345', False), ('Aa012345', False),
    ('Aa@12345', True), ('Aa#12345', True), ('Aa$12345', True), ('Aa%12345', True),
])
def test_password_character_partition(value, valid):
    assert bool(password_valid(value)) is valid
