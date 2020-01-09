import pytest
import autocomplete_server
import autocomplete_build
import json

from http import HTTPStatus


@pytest.fixture
def client():
    autocomplete_server.app.config['TESTING'] = True

    with autocomplete_server.app.test_client() as client:
        yield client


def test_health_check(client):
    response = client.get('/health')

    assert_status_code_ok(response)


def test_generate_completions(client):
    autocomplete_build.build()

    response = client.get('/autocomplete?q=how ca')

    assert_status_code_ok(response)

    response_body = parse_json_response(response)

    actual_completions = response_body['Completions']

    for completion in actual_completions:
        assert 'how' in completion.lower()

    response = client.get('/autocomplete?q=what is y')

    assert_status_code_ok(response)

    response_body = parse_json_response(response)

    actual_completions = response_body['Completions']

    for completion in actual_completions:
        assert 'what' in completion.lower()

    response = client.get('/autocomplete?q=when w')

    assert_status_code_ok(response)

    response_body = parse_json_response(response)

    actual_completions = response_body['Completions']

    for completion in actual_completions:
        assert 'when' in completion.lower()


def assert_status_code_ok(response):
    assert HTTPStatus.OK == response.status_code


def parse_json_response(response):
    formatted_json = response.data.decode('utf8').replace("'", '"')
    data = json.loads(formatted_json)

    return data
