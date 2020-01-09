""" Tests to validate that the autocompleter functions correctly.
    We are evaluating how you write unit tests, so please demonstrate your ability at writing
    good tests.  Feel free to add more tests to validate your solution. """

import os

from core.autocompleter import load_base_json, generate_elastic_search_input

JSON_DIR = os.getenv('BASE_JSON_DIR', '../sample_conversations.json')


def test_json_structure():
    issues = load_base_json(JSON_DIR)

    assert type(issues) == list

    expected_keys = ['IssueId', 'CompanyGroupId', 'Messages']
    expected_msg_keys = ['IsFromCustomer', 'Text']

    for issue in issues:
        assert type(issue) == dict

        actual_keys = list(issue.keys())

        assert expected_keys == actual_keys

        assert type(issue['IssueId']) == int
        assert type(issue['CompanyGroupId']) == int
        assert type(issue['Messages']) == list

        for msg in issue['Messages']:
            actual_msg_keys = list(msg.keys())

            assert expected_msg_keys == actual_msg_keys

            assert type(msg['IsFromCustomer']) == bool
            assert type(msg['Text']) == str


def test_message_generation():
    values = generate_elastic_search_input(JSON_DIR)

    expected_keys = ['_index', '_id', '_source']

    for v in values:
        actual_keys = list(v.keys())

        assert expected_keys == actual_keys
        assert type(v['_source']['message']) == str
