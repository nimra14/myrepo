import requests

def test_delete_user():
    base_url = "https://reqres.in/"
    session = requests.Session()

    # Make a DELETE request
    response = session.delete(base_url + "api/users/2")
    assert response.status_code == 204

    # Print the response details
    print(response.status_code)
    print(response.content)
