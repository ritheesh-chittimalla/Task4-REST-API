# Task4: REST-API
Building an REST API with Flask to perform operations.
This project implements a simple RESTful API using the Flask micro-framework to perform CRUD (Create, Read, Update, Delete) operations on in-memory user data.
🎯 Objective
The main goal is to build a REST API with Flask to manage user data, providing a foundational understanding of server-side API development and the principles of REST.

🛠 Tools Used
Python 

Flask (Web Framework)

Postman or cURL (API Testing)
📌 Features
GET /users → Fetch all users
GET /users/ → Fetch user by ID
POST /users → Create a new user
PUT /users/ → Update a user
DELETE /users/ → Delete a user
▶ How to Run
1. Clone the repo
bash git clone  cd task4-flask-rest-api

2. Install dependencies
bash pip install -r requirements.txt

3. Run the Flask app
bash python app.py

4. Test API Endpoints
Get all users
GET http://127.0.0.1:5000/users

Get user by ID
GET http://127.0.0.1:5000/users/1

Create a new user
POST http://127.0.0.1:5000/users

Update a user
PUT http://127.0.0.1:5000/users/1

Delete a user
DELETE http://127.0.0.1:5000/users/1

Outcome
Learned basics of REST API development using Flask

Implemented and tested CRUD operations

Practiced using Postman for API testing

Understood REST API workflow and project structure

Project structure
task4-flask-rest-api/ │ ├── app.py ├── requirements.txt ├── README.md └── screenshots/ ├── get-users.png ├── post-user.png ├── put-user.png └── delete-user.png
