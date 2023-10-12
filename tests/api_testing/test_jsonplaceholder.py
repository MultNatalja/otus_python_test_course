import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_status_code():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert len(data) > 0, "No comments found for post 1"


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_posts_by_post_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    data = response.json()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert "title" in data, "Response doesn't contain 'title' field"
    assert "body" in data, "Response doesn't contain 'body' field"
    assert "id" in data, "Response doesn't contain 'id' field"
    assert "userId" in data, "Response doesn't contain 'userId' field"


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_comments_count_for_comments_by_post_id(post_id):
    response = requests.get(f"{BASE_URL}/comments?postId={post_id}")
    data = response.json()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert len(data) > 0, f"No comments found for post {post_id}"


@pytest.mark.parametrize(("post_id", "title", "body", "userId"),
                         [(1, "title", "body", 1),
                         (2, "TITLE", "BODY", 2),
                         (3, "t", "b", 3)])
def test_put_posts_by_post_id(post_id, title, body, userId):
    data = {
        "id": post_id,
        "title": title,
        "body": body,
        "userId": userId
    }
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=data)
    response_data = response.json()
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response_data == data, f"Response data does not match expected data"


@pytest.mark.parametrize(("title", "body", "userId"),
                         [("TITLE", "B", 1),
                         ("T", "body3+Body/", 2),
                         ("title3+Title/", "BODY", 3)])
def test_post_posts_by_post_id(title, body, userId):
    data = {
        "title": title,
        "body": body,
        "userId": userId
    }
    response = requests.post(f"{BASE_URL}/posts", json=data)
    response_data = response.json()
    assert response.status_code == 201, f"Expected status code 201, but got {response.status_code}"
    assert response_data["title"] == title, f"Expected title {title}, but got {data['title']}"
    assert response_data["body"] == body, f"Expected title {body}, but got {data['body']}"
    assert response_data["userId"] == userId, f"Expected title {userId}, but got {data['userId']}"


@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_posts_by_post_id(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
