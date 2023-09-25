import json
from csv import DictReader

from src.reference import JSON_FILE, JSON_FILE_W
from src.reference import CSV_FILE


def get_users(file):
    data = []
    with open(file, "r") as f:
        users = json.load(f)
    for item in users:
        user = {
            "name": item["name"],
            "gender": item["gender"],
            "address": item["address"],
            "age": item["age"],
            "books": []
        }
        data.append(user)
    return data


def get_books(file):
    data = []
    with open(file, 'r', newline='') as f:
        reader = DictReader(f)
        books = list(reader)
    for book in books:
        book_data = {
            "title": book["Title"],
            "author": book["Author"],
            "pages": book["Pages"],
            "genre": book["Genre"]
        }
        data.append(book_data)
    return data


def make_result_file(json_file, csv_file, json_file_w):
    users_data = get_users(json_file)
    books_data = get_books(csv_file)

    user_index = 0
    for book in books_data:
        users_data[user_index]["books"].append(book)
        user_index = (user_index + 1) % len(users_data)

    with open(json_file_w, 'w') as f:
        s = json.dumps(users_data, indent=4)
        f.write(s)


make_result_file(JSON_FILE, CSV_FILE, JSON_FILE_W)
