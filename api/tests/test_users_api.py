from api.clients.user_client import UserClient
import pytest


@pytest.mark.api
@pytest.mark.regression
def test_get_user():

    client = UserClient()
    response = client.get_user(2)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["data"]["id"] == 2
    assert response_body["data"]["email"] is not None

@pytest.mark.api
@pytest.mark.regression
def test_create_user():

    client = UserClient()

    response = client.create_user(
        name="Tom",
        job="QA Engineer"
    )

    response_body = response.json()

    assert response.status_code == 201
    assert response_body["name"] == "Tom"
    assert response_body["job"] == "QA Engineer"
    assert "id" in response_body