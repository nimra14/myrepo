import requests

def test_get_users_details():
    base_url = "https://reqres.in/"
    session = requests.Session()

    # Make a GET request
    response = session.get(base_url + "api/users")
    assert response.status_code == 200

    # To validate Response body contains user i.e George
    body = response.json()
    assert "George" in body["data"][0]["first_name"]

    # To validate Headers contains Content-Type as application/json
    content_type_value = response.headers.get("Content-Type")
    assert content_type_value == "application/json; charset=utf-8"

    connection_value = response.headers.get("Connection")
    assert connection_value == "keep-alive"
