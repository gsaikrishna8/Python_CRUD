import logging
from database import cursor,conn
from schemas import UserCreate, UserUpdate
from models import *

logging.basicConfig(level= logging.DEBUG)

#create user
def create_user(user: UserCreate):
    try:
        #get last id
        cursor.execute('SELECT MAX(id) FROM Users')
        last_id = cursor.fetchone()[0] or 0
        new_id = last_id+1
        cursor.execute('SET IDENTITY_INSERT Users ON')
        cursor.execute('INSERT INTO Users (id, name, email) VALUES(?,?,?)',  (new_id, user.name, user.email) )
        cursor.execute('SET IDENTITY_INSERT Users OFF')
        conn.commit()
        return {"message": "User created Successfully", "id": new_id}
    except Exception as e:
        logging.error(f"Database error:{e}")
        return {"error":"Failed to create user"}

#read all users
def get_users():
    try:

        cursor.execute("SELECT * FROM Users")
        users = cursor.fetchall()
        return [{"id": row[0], "name":row[1], "email": row[2]} for  row in users]
    except Exception as e:
        logging.error(f"Database error:{e}")
        return {"error": "Failed to fetch Users"}
    
#Read user by  id
def get_user_byid(user_id: int):
    try:
        cursor.execute("SELECT * FROM Users WHERE id =? ", (user_id))
        user = cursor.fetchone()
        if user:
            return {"id": user[0], "name": user[1], "email": user[2]}
        return  {"error": "User not found"}
    except Exception as e:
        logging.error(f"Database error:{e}")
        return {"error": "User not found"}
    
#update user
def update_user(user_id: int, user: UserUpdate):
    try:
        cursor.execute("UPDATE Users SET name=?, email=? WHERE id =?  ", (user.name, user.email, user_id))
        conn.commit()
        return {"message": "User updated Successfully"}
    except Exception as e:
        logging.error(f"Database error:{e}")
        return {"error": "User not found"}
    

#Delete user
def delete_user(user_id:int):
    try:
        cursor.execute("DELETE FROM Users WHERE id=?", (user_id))
        conn.commit()
        return {"message": "User deleted successfully"}
    except Exception as e:
        logging.error(f"Database  error:{e}")
        return {"error":"User not found"}
