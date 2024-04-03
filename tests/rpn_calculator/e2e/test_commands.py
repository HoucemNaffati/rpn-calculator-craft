from starlette.testclient import TestClient

from src.rpn_calculator.web.main import build_fast_api_app

client = TestClient(build_fast_api_app())


def test_get_commands_200():
    response = client.get("/commands/")
    assert response.status_code == 200
    assert len(response.json()) > 0
