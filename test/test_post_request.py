import requests

def test_create_new_user():
    base_url = "https://reqres.in/"
    session = requests.Session()

    # Create the request body and headers
    body = {"name": "Asad.ALi", "job": "Test Engineer"}
    header = {"Content-Type": "application/json"}

    # Make a POST request
    response = session.post(base_url + "api/users", json=body, headers=header)

    # Check the status code
    actual_status_code = response.status_code
    expected_status_code = 201

    if actual_status_code != expected_status_code:
        print(f"Error: Expected status code {expected_status_code}, but got {actual_status_code}")
        print(response.content)

    assert actual_status_code == expected_status_code
