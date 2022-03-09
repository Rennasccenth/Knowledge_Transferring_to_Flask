from flask.testing import FlaskClient


def test_get_all_user(client: FlaskClient):
    response = client.get("/user")
    expected_response = []
