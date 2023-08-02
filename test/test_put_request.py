import requests

def test_update_user():
    base_url = "https://reqres.in"
    session = requests.Session()

    # Create the request body and headers
    body = {"name": "Ali", "job": "Engineer"}
    header = {"Content-Type": "application/json"}

    # Make a PUT request
    response = session.put(base_url + "/api/users/2", json=body, headers=header)
    assert response.status_code == 200

    # Print the response details
    print(response.status_code)
    print(response.content)
