import requests
import pytest

BASE_URL = "https://dog.ceo/api"


def test_random_dog_image_status_code():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"


def test_random_dog_image_response_structure():
    response = requests.get(f"{BASE_URL}/breeds/image/random")
    data = response.json()
    assert "message" in data, "Response doesn't contain 'message' field"
    assert "status" in data, "Response doesn't contain 'status' field"


@pytest.mark.parametrize("breed", ["bulldog", "beagle", "corgi", "pomeranian"])
def test_sub_breeds_structure(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/list")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary"
    assert "message" in data, "Response doesn't contain 'message' field"
    assert "status" in data, "Response doesn't contain 'status' field"
    assert isinstance(data["message"], list), "'message' field should be a list"


@pytest.mark.parametrize("breed", ["hound", "retriever", "akita", "dingo"])
def test_random_dog_images_by_breed_structure(breed):
    response = requests.get(f"{BASE_URL}/breed/{breed}/images/random/3")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary"
    assert "message" in data, "Response doesn't contain 'message' field"
    assert "status" in data, "Response doesn't contain 'status' field"
    assert isinstance(data["message"], list), "'message' field should be a list"
    assert all(url.startswith(f"https://images.dog.ceo/breeds/{breed}") for url in data["message"]), "Invalid image URLs"


def test_all_dog_breeds_structure():
    response = requests.get(f"{BASE_URL}/breeds/list/all")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    data = response.json()
    assert isinstance(data, dict), "Response should be a dictionary"
    assert "message" in data, "Response doesn't contain 'message' field"
    assert "status" in data, "Response doesn't contain 'status' field"
    assert isinstance(data["message"], dict), "'message' field should be a dictionary"
