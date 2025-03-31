Python CRUD API with FastAPI & Flask 
Overview
This project demonstrates how to build REST APIs using both FastAPI and Flask, implementing full CRUD (Create, Read, Update, Delete) operations with a SQL Server database.

Technologies Used
FastAPI – High-performance web framework

Flask – Lightweight and flexible web framework

SQL Server (SSMS) – Database for storing user data

SQLAlchemy – ORM for database interactions

Postman – API testing tool

Uvicorn – ASGI server for FastAPI

Project Structure

python-crud/
│── fastapi_app.py        # FastAPI application
│── flaskapi_app.py       # Flask application
│── database.py           # Database connection
│── models.py             # Database models
│── schemas.py            # Pydantic schemas for request validation
│── crud.py               # CRUD operations
│── .env                  # Environment variables (not committed)
│── requirements.txt      # Python dependencies
│── README.md             # Project documentation

Setup & Installation
1. Clone the Repository
git clone https://github.com/gsaikrishna8/Python_CRUD.git
cd Python_CRUD
2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Set Up the .env File
Create a .env file in the project root and add your SQL Server credentials:

DB_SERVER=your_sql_server
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
5. Run the API
FastAPI (Uvicorn Server)
uvicorn fastapi_app:app --reload
FastAPI will be available at: http://127.0.0.1:8000
Docs: http://127.0.0.1:8000/docs

Flask API
python flaskapi_app.py
Flask will be available at: http://127.0.0.1:5000

6. Test in Postman
Use Postman to test the following endpoints:

Method	Endpoint	Description
POST	/createuser/	Create a new user
GET	/users/	Retrieve all users
GET	/users/{id}	Get a user by ID
PUT	/users/{id}	Update a user
DELETE	/users/{id}	Delete a user
