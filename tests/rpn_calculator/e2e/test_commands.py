from starlette.testclient import TestClient

from src.rpn_calculator.web.main import app

client = TestClient(app)


def test_get_commands_200():
    response = client.get("/commands/")
    assert response.status_code == 200
    assert len(response.json()) > 0
