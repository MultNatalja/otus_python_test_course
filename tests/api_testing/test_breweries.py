import requests
import pytest

BASE_URL = "https://api.openbrewerydb.org"


def test_random_breweries_status_code():
    response = requests.get(f"{BASE_URL}/v1/breweries/random")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


@pytest.mark.parametrize("state", ["California", "New York"])
def test_search_breweries_by_state(state):
    response = requests.get(f"{BASE_URL}/breweries?by_state={state}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    for brewery in data:
        assert brewery["state"] == state, f"Brewery state does not match the expected state {state}"


@pytest.mark.parametrize(("brewery_id", "expected_name"),
                         [("06e9fffb-e820-45c9-b107-b52b51013e8f", "12Degree Brewing")])
def test_get_single_brewery_name(brewery_id, expected_name):
    response = requests.get(f"{BASE_URL}/breweries/{brewery_id}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert "name" in data, "Response doesn't contain 'name' field"
    assert data["name"] == expected_name, f"Expected name {expected_name}, but got {data['name']}"


@pytest.mark.parametrize("name", ["Sierra Nevada Brewing Co", "Brooklyn Brewery"])
def test_search_breweries_by_name(name):
    response = requests.get(f"{BASE_URL}/breweries?by_name={name}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    for brewery in data:
        assert name.lower() in brewery["name"].lower(), f"Brewery name does not contain the expected name {name}"


def test_get_random_brewery():
    response = requests.get(f"{BASE_URL}/v1/breweries/random")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert "id" in data[0], "Response doesn't contain 'id' field"
    assert "name" in data[0], "Response doesn't contain 'name' field"

