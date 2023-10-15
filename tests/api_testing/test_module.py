import requests


def test_check_url_status(url, status_code):
    response = requests.get(url)
    assert response.status_code == status_code, f"Expected status code {status_code}, but got {response.status_code}"
