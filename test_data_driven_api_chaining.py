import pytest
import requests
import allure

from utils.csv_reader import CSVReader
test_data = CSVReader.read_csv("books_test_data_10_rows.csv")
test_ids = [data["title"] for data in test_data] # to name the data 


BASE_URL = "https://library-api.postmanlabs.com"
API_KEY = "postmanrulz"


@allure.feature("Book API")
@allure.story("Data Driven End-to-End")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Validate complete Book API lifecycle using CSV test data.")
@pytest.mark.parametrize("data", test_data, ids=test_ids)
def test_book_end_to_end(data):

    headers = {
        "Content-Type": "application/json",
        "api-key": API_KEY
    }

    # -------------------------
    # 1. CREATE
    # -------------------------

    payload = {
        "title": data["title"],
        "author": data["author"],
        "genre": data["genre"],
        "yearPublished": int(data["yearPublished"])
    }

    create_response = requests.post(
        f"{BASE_URL}/books",
        json=payload,
        headers=headers,
        timeout=10
    )

    assert create_response.status_code == 201

    create_data = create_response.json()

    book_id = create_data["id"]

    print(f"\nCreated: {book_id}")

    try:

        # -------------------------
        # 2. GET
        # -------------------------

        get_response = requests.get(
            f"{BASE_URL}/books/{book_id}",
            headers=headers,
            timeout=10
        )

        assert get_response.status_code == 200

        get_data = get_response.json()

        assert get_data["id"] == book_id
        assert get_data["title"] == payload["title"]

        # -------------------------
        # 3. UPDATE
        # -------------------------

        update_payload = {
            "title": f"{payload['title']} Updated",
            "author": f"{payload['author']} Updated",
            "genre": payload["genre"],
            "yearPublished": payload["yearPublished"]
        }

        update_headers = {
            "Content-Type": "application/json",
            "api-key": API_KEY,
            "id": book_id
        }

        update_response = requests.patch(
            f"{BASE_URL}/books/{book_id}",
            json=update_payload,
            headers=update_headers,
            timeout=10
        )

        assert update_response.status_code == 200

        # -------------------------
        # 4. VERIFY UPDATE
        # -------------------------

        verify_response = requests.get(
            f"{BASE_URL}/books/{book_id}",
            headers=headers,
            timeout=10
        )

        assert verify_response.status_code == 200

        verify_data = verify_response.json()

        assert verify_data["title"] == update_payload["title"]
        assert verify_data["author"] == update_payload["author"]

        # -------------------------
        # 5. DELETE
        # -------------------------

        delete_response = requests.delete(
            f"{BASE_URL}/books/{book_id}",
            headers=update_headers,
            timeout=10
        )

        assert delete_response.status_code in (200, 204)

        # -------------------------
        # 6. VERIFY DELETE
        # -------------------------

        final_response = requests.get(
            f"{BASE_URL}/books/{book_id}",
            headers=headers,
            timeout=10
        )

        assert final_response.status_code == 404

    finally:

        # Safety cleanup
        requests.delete(
            f"{BASE_URL}/books/{book_id}",
            headers=update_headers,
            timeout=10
        )