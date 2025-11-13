# CRUD Using HTTP Requests (With a Real API Example)

This note explains **CRUD** operations — **Create, Read, Update, Delete** — using real HTTP requests to an actual public test API. It is written so that a beginner student can follow and try everything themselves.

We will use this free, public API for practice:

> `https://jsonplaceholder.typicode.com`

This is a **fake online REST API** for testing and learning. You can call it from your browser, Postman, or Python/JavaScript code.

We’ll work with the `/posts` endpoint as our example resource (like blog posts or records in a database).

---

## 1. READ – Getting Data (GET Request)

### 1.1 Get all posts

* **Method:** `GET`
* **URL:** `https://jsonplaceholder.typicode.com/posts`
* **Meaning:** "Give me the list of all posts."

Try in your browser:

* Open: `https://jsonplaceholder.typicode.com/posts`

Example response (shortened):

```json
[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati",
    "body": "quia et suscipit..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore..."
  }
]
```

### 1.2 Get a single post by ID

* **Method:** `GET`
* **URL:** `https://jsonplaceholder.typicode.com/posts/1`

Example (using `curl` in terminal):

```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

---

## 2. CREATE – Adding New Data (POST Request)

To **create** a new post, we send a **POST** request with a JSON body.

* **Method:** `POST`
* **URL:** `https://jsonplaceholder.typicode.com/posts`
* **Headers:** `Content-Type: application/json`
* **Body (JSON):**

```json
{
  "title": "My first test post",
  "body": "This is created from an API call.",
  "userId": 1
}
```

### Example with `curl`

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My first test post",
    "body": "This is created from an API call.",
    "userId": 1
  }'
```

Example response:

```json
{
  "title": "My first test post",
  "body": "This is created from an API call.",
  "userId": 1,
  "id": 101
}
```

> Note: JSONPlaceholder doesn’t really save it in a database, but it pretends (for learning).

---

## 3. UPDATE – Modifying Existing Data (PUT and PATCH)

There are two common ways to update:

* **PUT** – replace the whole object.
* **PATCH** – change only some fields.

### 3.1 Update a post completely (PUT)

* **Method:** `PUT`
* **URL:** `https://jsonplaceholder.typicode.com/posts/1`
* **Body (JSON):**

```json
{
  "id": 1,
  "title": "Updated title",
  "body": "Updated content of the post.",
  "userId": 1
}
```

Example with `curl`:

```bash
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "id": 1,
    "title": "Updated title",
    "body": "Updated content of the post.",
    "userId": 1
  }'
```

### 3.2 Update only one field (PATCH)

* **Method:** `PATCH`
* **URL:** `https://jsonplaceholder.typicode.com/posts/1`
* **Body (JSON):**

```json
{
  "title": "Partially updated title"
}
```

Example with `curl`:

```bash
curl -X PATCH https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Partially updated title"
  }'
```

---

## 4. DELETE – Removing Data (DELETE Request)

To delete a post:

* **Method:** `DELETE`
* **URL:** `https://jsonplaceholder.typicode.com/posts/1`

Example with `curl`:

```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

The API typically returns an empty object `{}` to indicate a successful deletion.

---

## 5. CRUD Summary Table

| Operation | HTTP Method | Example URL                                    | Request Body? | Typical Use            |
| --------- | ----------- | ---------------------------------------------- | ------------- | ---------------------- |
| Create    | POST        | `https://jsonplaceholder.typicode.com/posts`   | Yes (JSON)    | Add a new record       |
| Read      | GET         | `https://jsonplaceholder.typicode.com/posts/1` | No            | Get existing data      |
| Update    | PUT/PATCH   | `https://jsonplaceholder.typicode.com/posts/1` | Yes (JSON)    | Modify existing record |
| Delete    | DELETE      | `https://jsonplaceholder.typicode.com/posts/1` | No            | Remove existing record |

---

## 6. Using a Real API in Code (Python Example)

Below is a simple example using **Python** and the `requests` library.

### 6.1 Install the library (if needed)

```bash
pip install requests
```

### 6.2 Python code for basic CRUD

```python
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

# 1. READ – Get all posts
response = requests.get(BASE_URL)
print("All posts status:", response.status_code)
print(response.json()[:2])  # print first two posts

# 2. CREATE – Add a new post
new_post = {
    "title": "Student CRUD Example",
    "body": "Created from Python code",
    "userId": 1
}
create_res = requests.post(BASE_URL, json=new_post)
print("Create status:", create_res.status_code)
print(create_res.json())

# 3. UPDATE – Change the title using PATCH
update_data = {"title": "Updated from Python"}
update_res = requests.patch(f"{BASE_URL}/1", json=update_data)
print("Update status:", update_res.status_code)
print(update_res.json())

# 4. DELETE – Delete a post
delete_res = requests.delete(f"{BASE_URL}/1")
print("Delete status:", delete_res.status_code)
print(delete_res.text)
```

---

## 7. How This Maps to a Real Student App

Imagine you are building a **Student Management System**. Instead of `/posts`, you might have:

* `GET /students` → list all students
* `GET /students/10` → get student with ID 10
* `POST /students` → create a new student
* `PUT /students/10` → update full student info
* `PATCH /students/10` → update only some fields
* `DELETE /students/10` → remove a student

The logic is **exactly the same** as in this note — only the endpoint and data fields (like `name`, `roll`, `class`, etc.) change.

---

## 8. Key Points for Students

* **CRUD** = Create, Read, Update, Delete.
* Done over the web using HTTP methods: **POST, GET, PUT/PATCH, DELETE**.
* Data is usually sent/received as **JSON**.
* You can practice safely using a test API like **JSONPlaceholder** before connecting to a real backend you build yourself.

You can now use this as a quick reference while coding your first CRUD project using HTTP requests.
