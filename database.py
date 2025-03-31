import pyodbc
import os
from dotenv import load_dotenv


DB_SERVER= os.getenv("DB_SERVER")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

#connection string
conn =  pyodbc.connect(
     f"DRIVER={{SQL Server}}; SERVER={DB_SERVER}; DATABASE={DB_NAME}; UID={DB_USER}; PWD={DB_PASSWORD}"
)
cursor = conn.cursor()
