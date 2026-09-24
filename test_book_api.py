import uuid
import time

import allure
import pytest
import requests

# Values taken from the uploaded test_api.py:
# BASE_URL = https://library-api.postmanlabs.com
# API_KEY = postmanrulz
BASE_URL = "https://library-api.postmanlabs.com"
API_KEY = "postmanrulz"
BOOKS_URL = f"{BASE_URL}/books"
TIMEOUT = 10


def api_headers(api_key=API_KEY, book_id=None, content_type="application/json"):
    headers = {"api-key": api_key}
    if content_type is not None:
        headers["Content-Type"] = content_type
    if book_id:
        headers["id"] = book_id
    return headers


def valid_book_payload(suffix=None):
    suffix = suffix or uuid.uuid4().hex[:8]
    return {
        "title": f"Learning API {suffix}",
        "author": "Prashant Pardeshi",
        "genre": "computers",
        "yearPublished": 2026,
    }


def create_book():
    payload = valid_book_payload()
    response = requests.post(
        BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
    )
    return response, payload


@pytest.fixture
def created_book():
    response, payload = create_book()
    assert response.status_code == 201, (
        f"Book setup failed: {response.status_code} - {response.text}"
    )
    data = response.json()
    assert "id" in data
    book_id = data["id"]

    yield {"id": book_id, "payload": payload, "data": data}

    cleanup = requests.delete(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    if cleanup.status_code not in (200, 204, 404):
        print(f"Cleanup warning: {cleanup.status_code} - {cleanup.text}")


@pytest.fixture
def deleted_book():
    response, payload = create_book()
    assert response.status_code == 201
    book_id = response.json()["id"]

    delete_response = requests.delete(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert delete_response.status_code in (200, 204)
    return {"id": book_id, "payload": payload}


@allure.feature("Book API")
@allure.story("Create Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that a book can be created successfully with valid data.")
@allure.step("Create a book with valid data and verify HTTP 201")
def test_tc01_create_book_valid_data():
    response, payload = create_book()
    try:
        assert response.status_code == 201, response.text
        data = response.json()
        assert "id" in data
        assert data["title"] == payload["title"]
        assert data["author"] == payload["author"]
        assert data["genre"] == payload["genre"]
        assert data["yearPublished"] == payload["yearPublished"]
    finally:
        if response.status_code == 201:
            book_id = response.json().get("id")
            if book_id:
                requests.delete(
                    f"{BOOKS_URL}/{book_id}",
                    headers=api_headers(book_id=book_id),
                    timeout=TIMEOUT,
                )


@allure.feature("Book API")
@allure.story("Get Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that an existing book can be retrieved using its ID.")
@allure.step("Create a book, retrieve it using its ID, and verify HTTP 200")
def test_tc02_get_existing_book(created_book):
    book_id = created_book["id"]
    response = requests.get(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    assert data["title"] == created_book["payload"]["title"]


@allure.feature("Book API")
@allure.story("Update Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that complete book data can be updated successfully.")
@allure.step("Update an existing book and verify HTTP 200")
def test_tc03_update_book_complete_data(created_book):
    book_id = created_book["id"]
    update_payload = {
        "title": "Learning API Updated",
        "author": "Prashant Pardeshi Updated",
        "genre": "automation",
        "yearPublished": 2027,
    }
    response = requests.patch(
        f"{BOOKS_URL}/{book_id}",
        json=update_payload,
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == book_id
    for key, value in update_payload.items():
        assert data[key] == value


@allure.feature("Book API")
@allure.story("Verify Updated Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify updated book data by retrieving the book again using GET.")
@allure.step("Update a book, retrieve it using GET, and verify updated data")
def test_tc04_verify_updated_data_using_get(created_book):
    book_id = created_book["id"]
    update_payload = {
        "title": "Updated Through GET Verification",
        "author": "Prashant Updated",
        "genre": "testing",
        "yearPublished": 2028,
    }
    update_response = requests.patch(
        f"{BOOKS_URL}/{book_id}",
        json=update_payload,
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert update_response.status_code == 200

    get_response = requests.get(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["id"] == book_id
    for key, value in update_payload.items():
        assert data[key] == value


@allure.feature("Book API")
@allure.story("Delete Book")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that an existing book can be deleted successfully.")
@allure.step("Create a book, delete it, and verify HTTP 200 or 204")
def test_tc05_delete_existing_book(created_book):
    book_id = created_book["id"]
    response = requests.delete(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert response.status_code in (200, 204)


@allure.feature("Book API")
@allure.story("Get Deleted Book")
@allure.severity(allure.severity_level.HIGH)
@allure.description("Verify that retrieving a deleted book returns HTTP 404.")
@allure.step("Delete a book and verify GET returns HTTP 404")
def test_tc06_get_deleted_book(deleted_book):
    book_id = deleted_book["id"]
    response = requests.get(
        f"{BOOKS_URL}/{book_id}",
        headers=api_headers(book_id=book_id),
        timeout=TIMEOUT,
    )
    assert response.status_code == 404


@allure.feature("Book API")
@allure.story("Negative Get Book")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that an invalid/non-existing book ID returns HTTP 404.")
@allure.step("Request a non-existing book ID and verify HTTP 404")
def test_tc07_get_invalid_book_id():
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = requests.get(
        f"{BOOKS_URL}/{invalid_id}",
        headers=api_headers(book_id=invalid_id),
        timeout=TIMEOUT,
    )
    assert response.status_code == 404


@allure.feature("Book API")
@allure.story("Negative Create Book")
@allure.severity(allure.severity_level.HIGH)
@allure.description("Verify that creating a book without a mandatory field is rejected.")
@allure.step("Create a book without the title field and verify HTTP 400 or 422")
def test_tc08_create_book_missing_mandatory_field():
    payload = valid_book_payload()
    payload.pop("title")
    response = requests.post(
        BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
    )
    assert response.status_code in (400, 422), response.text


@allure.feature("Book API")
@allure.story("Negative Create Book")
@allure.severity(allure.severity_level.HIGH)
@allure.description("Verify that invalid field data types are rejected.")
@allure.step("Send an invalid data type for yearPublished and verify HTTP 400 or 422")
def test_tc09_create_book_invalid_data_type():
    payload = valid_book_payload()
    payload["yearPublished"] = "twenty twenty-six"
    response = requests.post(
        BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
    )
    assert response.status_code in (400, 422), response.text


@allure.feature("Book API")
@allure.story("Duplicate Book")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify the API-defined behavior when duplicate book data is submitted.")
@allure.step("Create the same book twice and verify duplicate/conflict behavior")
def test_tc10_duplicate_book_business_conflict():
    payload = valid_book_payload("duplicate")
    first_response = requests.post(
        BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
    )
    assert first_response.status_code == 201
    first_book_id = first_response.json().get("id")
    try:
        second_response = requests.post(
            BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
        )
        # The exact behavior is API-contract dependent; 409 is common.
        assert second_response.status_code in (400, 409, 422), second_response.text
    finally:
        if first_book_id:
            requests.delete(
                f"{BOOKS_URL}/{first_book_id}",
                headers=api_headers(book_id=first_book_id),
                timeout=TIMEOUT,
            )


@allure.feature("Book API")
@allure.story("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that a request without an API key is rejected with HTTP 401 or 403.")
@allure.step("Send a request without the API key and verify HTTP 401 or 403")
def test_tc11_missing_api_key():
    response = requests.get(
        BOOKS_URL,
        headers={"Content-Type": "application/json"},
        timeout=TIMEOUT,
    )
    assert response.status_code in (401, 403), response.text


@allure.feature("Book API")
@allure.story("Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify that an invalid API key is rejected with HTTP 401 or 403.")
@allure.step("Send a request with an invalid API key and verify HTTP 401 or 403")
def test_tc12_invalid_api_key():
    response = requests.get(
        BOOKS_URL,
        headers=api_headers(api_key="invalid-api-key"),
        timeout=TIMEOUT,
    )
    assert response.status_code in (401, 403), response.text


@allure.feature("Book API")
@allure.story("HTTP Method Validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that an unsupported HTTP method returns HTTP 405.")
@allure.step("Send an unsupported HTTP method and verify HTTP 405")
def test_tc13_unsupported_http_method():
    response = requests.put(
        BOOKS_URL, json=valid_book_payload(), headers=api_headers(), timeout=TIMEOUT
    )
    assert response.status_code == 405, response.text


@allure.feature("Book API")
@allure.story("Header Validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that an unsupported Content-Type is rejected with HTTP 415.")
@allure.step("Send JSON data with invalid Content-Type and verify HTTP 415")
def test_tc14_invalid_content_type():
    response = requests.post(
        BOOKS_URL,
        data='{"title":"Invalid Content Type"}',
        headers=api_headers(content_type="text/plain"),
        timeout=TIMEOUT,
    )
    assert response.status_code == 415, response.text


@allure.feature("Book API")
@allure.story("Payload Validation")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that an excessively large/invalid payload returns an API-defined 4xx response.")
@allure.step("Send an excessively large title and verify an API-defined 4xx response")
def test_tc15_large_invalid_payload():
    payload = valid_book_payload()
    payload["title"] = "A" * 1_000_000
    response = requests.post(
        BOOKS_URL, json=payload, headers=api_headers(), timeout=TIMEOUT
    )
    assert 400 <= response.status_code < 500, (
        f"Expected 4xx, got {response.status_code}: {response.text[:500]}"
    )


@allure.feature("Book API")
@allure.story("Response Schema")
@allure.severity(allure.severity_level.HIGH)
@allure.description("Verify that book responses contain the expected fields and data types.")
@allure.step("Get books and validate response schema")
def test_tc16_response_schema_validation():
    response = requests.get(BOOKS_URL, headers=api_headers(), timeout=TIMEOUT)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

    required_fields = {
        "id": str,
        "title": str,
        "author": str,
        "genre": str,
        "yearPublished": int,
        "checkedOut": bool,
        "isPermanentCollection": bool,
        "createdAt": str,
    }
    for book in data:
        for field, expected_type in required_fields.items():
            assert field in book, f"Missing field: {field}"
            assert isinstance(book[field], expected_type), (
                f"{field} should be {expected_type.__name__}, "
                f"got {type(book[field]).__name__}"
            )


@allure.feature("Book API")
@allure.story("Performance")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that GET /books responds within the agreed 1-second SLA.")
@allure.step("Send GET /books and verify response time is below 1 second")
def test_tc17_response_time():
    response = requests.get(BOOKS_URL, headers=api_headers(), timeout=TIMEOUT)
    response_time = response.elapsed.total_seconds()
    assert response.status_code == 200
    assert response_time < 1, f"Response time too long: {response_time:.3f}s"


@allure.feature("Book API")
@allure.story("Response Headers")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify that the response contains the expected JSON Content-Type header.")
@allure.step("Get books and verify response headers")
def test_tc18_verify_headers():
    response = requests.get(BOOKS_URL, headers=api_headers(), timeout=TIMEOUT)
    assert response.status_code == 200
    content_type = response.headers.get("Content-Type", "")
    assert content_type.startswith("application/json"), content_type


@allure.feature("Book API")
@allure.story("Rate Limiting")
@allure.severity(allure.severity_level.LOW)
@allure.description("Verify that HTTP 429 is returned when the configured API rate limit is exceeded.")
@allure.step("Send repeated requests and verify HTTP 429 when the limit is exceeded")
def test_tc19_rate_limiting():
    responses = []
    for _ in range(100):
        response = requests.get(BOOKS_URL, headers=api_headers(), timeout=TIMEOUT)
        responses.append(response)
        if response.status_code == 429:
            break
        time.sleep(0.05)

    assert any(r.status_code == 429 for r in responses), (
        "HTTP 429 was not observed within 100 requests. "
        "Adjust the loop according to the API rate-limit contract."
    )


@allure.feature("Book API")
@allure.story("API Chaining")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify Create -> ID extraction -> Update -> GET -> Delete chaining using a dynamic book ID.")
@allure.step("Create -> extract ID -> update -> GET -> delete using the same dynamic ID")
def test_tc20_api_chaining():
    create_response, _ = create_book()
    assert create_response.status_code == 201
    book_id = create_response.json()["id"]

    try:
        update_payload = {
            "title": "Chained API Book Updated",
            "author": "Prashant Pardeshi",
            "genre": "api-automation",
            "yearPublished": 2029,
        }
        update_response = requests.patch(
            f"{BOOKS_URL}/{book_id}",
            json=update_payload,
            headers=api_headers(book_id=book_id),
            timeout=TIMEOUT,
        )
        assert update_response.status_code == 200
        assert update_response.json()["id"] == book_id

        get_response = requests.get(
            f"{BOOKS_URL}/{book_id}",
            headers=api_headers(book_id=book_id),
            timeout=TIMEOUT,
        )
        assert get_response.status_code == 200
        assert get_response.json()["id"] == book_id
        assert get_response.json()["title"] == update_payload["title"]

        delete_response = requests.delete(
            f"{BOOKS_URL}/{book_id}",
            headers=api_headers(book_id=book_id),
            timeout=TIMEOUT,
        )
        assert delete_response.status_code in (200, 204)

        verify_response = requests.get(
            f"{BOOKS_URL}/{book_id}",
            headers=api_headers(book_id=book_id),
            timeout=TIMEOUT,
        )
        assert verify_response.status_code == 404
    finally:
        # Cleanup if the chain failed before deletion.
        requests.delete(
            f"{BOOKS_URL}/{book_id}",
            headers=api_headers(book_id=book_id),
            timeout=TIMEOUT,
        )
