import pytest
from httpx import Response
from starlette.testclient import TestClient

from src.rpn_calculator.web.main import build_fast_api_app


@pytest.fixture()
def http_test_client():
    app = build_fast_api_app()
    client = TestClient(app)
    yield client  # provides a fresh app and client for each test


@pytest.mark.parametrize("test_input", [1.1, "A", "!", "12c", "a007"])
def test_post_stack_values_400(http_test_client: TestClient, test_input: any):
    response = post_new_stack_value(http_test_client, test_input)
    assert response.status_code == 400


def test_post_stack_values_201(http_test_client: TestClient):
    response = post_new_stack_value(http_test_client, "1")
    assert response.status_code == 201
    assert response.headers["Location"] == "/stack/"
    assert response.json() == {}


@pytest.mark.parametrize("test_input", ["a", "0", ""])
def test_put_stack_command_400(http_test_client: TestClient, test_input: str):
    response = put_stack_command(http_test_client, test_input)
    assert response.status_code == 400


@pytest.mark.parametrize("test_input", ["+", "-", "*"])
def test_put_stack_command_when_not_enough_elements_422(
    http_test_client: TestClient, test_input: str
):
    response = put_stack_command(http_test_client, test_input)
    assert response.status_code == 422


@pytest.mark.parametrize("test_input", ["+", "-", "*"])
def test_put_stack_command_201(http_test_client, test_input: str):
    append_stack_elements(http_test_client, 0, 0)
    response = put_stack_command(http_test_client, test_input)
    assert response.status_code == 201
    assert response.headers["Location"] == "/stack"
    assert response.json() == {}


def append_stack_elements(client: TestClient, *elements: [int]):
    for element in elements:
        response = post_new_stack_value(client, element)
        assert response.status_code == 201


def post_new_stack_value(client: TestClient, value: str) -> Response:
    return client.post("/stack/values", json={"value": f"{value}"})


def put_stack_command(client: TestClient, value: str) -> Response:
    return client.put("/stack", json={"command": f"{value}"})
