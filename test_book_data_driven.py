from utils.csv_reader import CSVReader
test_data = CSVReader.read_csv("books_test_data_10_rows.csv")

import pytest
import requests


BASE_URL = "https://library-api.postmanlabs.com"
API_KEY = "postmanrulz"

test_ids = [data["title"] for data in test_data] # to name the data 

# @pytest.mark.parametrize("data", test_data) # without test data name
@pytest.mark.parametrize("data", test_data, ids=test_ids)
def test_create_book_data_driven(data):

    url = f"{BASE_URL}/books"

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    payload = {
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
        "yearPublished": int(data["yearPublished"])
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=10
    )

    # Status validation
    assert response.status_code == 201, response.text

    response_data = response.json()

    # ID validation
    assert "id" in response_data

    # Response validation
    assert response_data["title"] == payload["title"]
    assert response_data["author"] == payload["author"]
    assert response_data["genre"] == payload["genre"]
    assert response_data["yearPublished"] == payload["yearPublished"]

    print(
        f"Created book: {response_data['title']} "
        f"| ID: {response_data['id']}"
    )