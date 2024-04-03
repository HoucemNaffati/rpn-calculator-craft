import pytest
from httpx import Response
from starlette.testclient import TestClient

from src.rpn_calculator.web.main import app

client = TestClient(app)


@pytest.mark.parametrize("test_input", [1.1, "A", "!", "12c", "a007"])
def test_post_stack_values_400(test_input):
    response = post_new_stack_value(test_input)
    assert response.status_code == 400


@pytest.mark.parametrize("test_input", [1])
def test_post_stack_values_201(test_input):
    response = post_new_stack_value(test_input)
    assert response.status_code == 201
    assert response.headers["Location"] == "/stack/"
    assert response.json() == {}


def post_new_stack_value(value: any) -> Response:
    response = client.post("/stack/values", json={"value": f"{value}"})
    return response
