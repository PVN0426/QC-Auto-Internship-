import requests


def test_connection():

    response = requests.post(
        "https://restful-booker.herokuapp.com/auth",
        json={
            "username": "admin",
            "password": "password123"
        },
        verify=False
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code == 200