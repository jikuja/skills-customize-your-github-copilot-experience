# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using the FastAPI framework, practicing route creation, request handling, and returning JSON responses.

## 📝 Tasks

### 🛠️	Create a Basic FastAPI App

#### Description
Set up a FastAPI application with a few routes that return JSON data. This is the foundation for everything that follows.

#### Requirements
Completed program should:

- Import and instantiate a `FastAPI` app
- Define a `GET /` route that returns a welcome message as JSON
- Define a `GET /items` route that returns a hardcoded list of items
- Run the app using `uvicorn`

### 🛠️	Add Path and Query Parameters

#### Description
Extend your API to support dynamic URLs and optional query parameters so callers can request specific data.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` route that returns a single item by its ID
- Return a `404` error response when the item ID does not exist
- Add an optional `?search=` query parameter to the `GET /items` route that filters items by name

### 🛠️	Handle POST Requests with a Request Body

#### Description
Allow clients to create new items by sending data in the request body using a Pydantic model.

#### Requirements
Completed program should:

- Define a Pydantic model for an item with at least `id`, `name`, and `price` fields
- Define a `POST /items` route that accepts the model as the request body
- Add the new item to the in-memory list and return the created item
- Return a `400` error response if an item with the same ID already exists
