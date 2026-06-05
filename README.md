# Contact Book API

## Project Overview

Contact Book API is a backend application developed using FastAPI and MySQL. It allows users to manage contact information by performing Create, Read, Update, Delete, and Search operations through RESTful APIs.        

The project demonstrates FastAPI fundamentals such as API routing, request validation using Pydantic, database connectivity with MySQL, and API testing using Swagger UI.

---

## Features

* Add a new contact
* View all contacts
* View a contact by ID   
* Update contact details   
* Delete a contact
* Search contacts by name
* Automatic API documentation using Swagger UI

---

## Technologies Used

* Python
* FastAPI
* MySQL
* Pydantic
* Uvicorn

---

## Project Structure

```text
contact_book/
│
├── main.py
├── db.py
├── models.py
└── README.md
```

### main.py

Contains all API endpoints and business logic.

### db.py

Establishes a connection with the MySQL database.

### models.py

Contains Pydantic models used for request validation.    

---

## Database Schema

### Contacts Table

```sql
CREATE TABLE contacts(
    contact_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    phone VARCHAR(100),
    email VARCHAR(100)
);
```

---

## API Endpoints

### Add Contact

```http
POST /contact
```

Adds a new contact to the database.

### Get All Contacts

```http
GET /contacts
```

Retrieves all contacts from the database.

### Get Contact By ID

```http
GET /contacts/{contact_id}
```

Retrieves a specific contact using its ID.

### Update Contact

```http
PUT /contacts/{contact_id}
```

Updates the details of an existing contact.

### Delete Contact

```http
DELETE /contacts/{contact_id}
```

Deletes a contact from the database.

### Search Contact

```http
GET /search?name=value
```

Searches contacts by name.

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd contact_book
```

### Install Dependencies

```bash
pip install fastapi uvicorn mysql-connector-python
```

### Configure Database

Create a MySQL database named:

```sql
contact_book
```

Create the contacts table using the provided schema.

Update the database credentials in `db.py`.

---

## Running the Application

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

These interfaces can be used to test and interact with all API endpoints.

---

## Learning Outcomes

Through this project, the following concepts were implemented:

* REST API Development
* FastAPI Routing
* Pydantic Validation
* MySQL Database Integration
* CRUD Operations
* Query Parameters
* API Documentation with Swagger UI
* Database Connection Handling

---

## Future Enhancements

* User Authentication using JWT
* Contact Categories
* Pagination
* Email Validation
* Contact Import and Export
* Profile Images for Contacts

---

## Author

**Nandini**

Python Backend Developer

Skills: Python, FastAPI, Flask, Django, MySQL, HTML, CSS, JavaScript
