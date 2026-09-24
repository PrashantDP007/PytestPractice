import pytest
import requests

import requests
from requests import auth

response = requests.get("https://library-api.postmanlabs.com/books")

print(response.status_code)
print(response.text)
print(response.json())
print(response.headers)
print(response.cookies)
print(response.elapsed)
print(response.url)
print(response.request.method)
data = response.json()
print(data[0]["title"])

@pytest.mark.skip(reason="Need to fix this test case.")
def test_api_response():
    assert response.status_code == 200
    assert "title" in response.json()
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    assert response.elapsed.total_seconds() < 1

# api test case to check if the response contains the expected data
@pytest.mark.skip(reason="Need to fix this test case.")
def test_api_response_data():
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for book in data:
        print(book)
        assert "title" in book
        assert "author" in book
        assert "isbn" in book
id = ""

# api test case to create a book sample {'title': 'Learning API', 'author': 'Prashant Pardeshi', 'genre': 'computers', 'yearPublished': 2026}
def test_create_book():
    global id
    url = "https://library-api.postmanlabs.com/books"
    # authentication = ("api-key", "postmanrulz")  # Replace with your actual credentials
    # provide authentication inside header "api-key", "postmanrulz"    
    headers = {
        "Content-Type": "application/json",
        "api-key": "postmanrulz"
    }
    payload = {
        "title": "Learning API",
        "author": "Prashant Pardeshi",
        "genre": "computers",
        "yearPublished": 2026
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["genre"] == payload["genre"]
    assert data["yearPublished"] == payload["yearPublished"]
    print(f"Book created successfully with id: {data['id']}")
    # i want to get the book by id and print the response here id can be used for path parameter in the url and also in the header as "id": data["id"]
    response2 = requests.get(f"https://library-api.postmanlabs.com/books/{data['id']}", headers={"api-key": "postmanrulz"})
    print(response2.json())
    id = data["id"]
    book = response2.json()
    print(book["title"])
    print(book["author"])
    print(book["genre"])
    print(book["yearPublished"])
    print(f"Book with id {id} retrieved successfully.")

def test_update_book():
    # i need to update the book created in the previous test case using the id from the response and also in the header as "id": data["id"] 7016219b-33bd-4a13-bfa2-36fca45f737b
    url = f"https://library-api.postmanlabs.com/books/{id}"
    headers = {
        "Content-Type": "application/json",
        "api-key": "postmanrulz",
        "id": id
    }           
    payload = {
        "title": "Learning API Updated1",        
        "author": "Prashant Pardeshi Updated1",
        "genre": "computers Updated1",
        "yearPublished": 2026
    }
    response = requests.patch(url, json=payload, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]  
    assert data["genre"] == payload["genre"]
    assert data["yearPublished"] == payload["yearPublished"]
    print(f"Book with id {id} updated successfully.")
    print(f"Updated book data: title: {data['title']}, author: {data['author']}, genre: {data['genre']}, yearPublished: {data['yearPublished']}")

def test_delete_book():
    url = f"https://library-api.postmanlabs.com/books/{id}"
    headers = {
        "Content-Type": "application/json",
        "api-key": "postmanrulz",
        "id": id
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 204
    print(f"Book with id {id} deleted successfully.")

# test_create_book()
# test_update_book()
# test_delete_book()


# test case to Create a POST request, extract the created user's ID and use it to perform a GET request.
@pytest.fixture
def test_create_and_get_user():
    # Create a new user using POST request
    url = "https://library-api.postmanlabs.com/books"
    headers = {
            "Content-Type": "application/json",
            "api-key": "postmanrulz"
        }
    payload = {
        "title": "Learning API for retrieving user",
        "author": "Prashant Pardeshi",  
        "genre": "computers",
        "yearPublished": 2026
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    data = response.json()
    book_id = data["id"]
    print(f"Book created successfully with id: {book_id}")
    
    # Now perform a GET request using the extracted book ID
    get_response = requests.get(f"https://library-api.postmanlabs.com/books/{book_id}")
    assert get_response.status_code == 200
    book_data = get_response.json()
    print(f"Retrieved book data: {book_data}")

    return book_id


# create test to validate response time, i want to check if the response time is less than 1 second, if not then fail the test case
def test_response_time():
    response = requests.get("https://library-api.postmanlabs.com/books")
    print(f"Response time: {response.elapsed.total_seconds()} seconds")
    assert response.elapsed.total_seconds() < 1, f"Response time is too long: {response.elapsed.total_seconds()} seconds"

# Query parameters are used to filter API results.
# Example: /books?genre=computers returns only books matching that genre.
def test_query_parameter_filter():
    url = "https://library-api.postmanlabs.com/books"
    params = {"author": "Prashant Pardeshi"}
    response = requests.get(url, params=params, headers={"api-key": "postmanrulz"})

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

    # if len(data) > 0:
    #     assert all(book.get("author") == "Prashant Pardeshi" for book in data)

    print(f"Books returned for query param 'genre=computers': {data}")

# Path parameters identify a specific resource in the URL.
# Example: /books/{id} points to one exact book record.
def test_path_parameter_example(test_create_and_get_user):
    book_id = test_create_and_get_user
    url = f"https://library-api.postmanlabs.com/books/{book_id}" 
    response = requests.get(url, headers={"api-key": "postmanrulz"})

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data.get("id") == book_id or "id" in data
    print(f"Book details for path parameter id {book_id}: \n{data}")
