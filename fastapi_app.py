from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from  schemas import UserCreate, UserUpdate
import crud
import logging

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

#Global exception  Handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"Unhandled error at {request.url}: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "details": str(exc)},
    )

#Root Route
@app.get("/")
def root():
    return{"message":"Welcome to Fast api"}

#Create User
@app.post("/createuser/")
def create_user(user: UserCreate):
    result = crud.create_user(user)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result['error'])
    return result

#Get  all users
@app.get("/users/")
def get_users():
    return crud.get_users()

#get user by Id
@app.get("/users/{user_id}")
def get_user_by_id(user_id:int):
    user = crud.get_user_byid(user_id)
    if 'error' in user:
        raise HTTPException(status_code=404, detail='user not found')
    return user

# update user
@app.put("/users/{user_id}")
def update_user(user_id:int, user: UserUpdate):
    result = crud.update_user(user_id, user)
    if "error" in result:
        raise HTTPException(status_code=400, detail= result["error"])
    return result

#Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    result = crud.delete_user(user_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result    