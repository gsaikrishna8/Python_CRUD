from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import crud
from schemas import  UserCreate, UserUpdate
from pydantic import ValidationError

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

@app.errorhandler(Exception)
def global_exception_handler(error):
    logging.error(f"Unhandled error: {error}")
    return jsonify({"error": "Internal server error", "details": str(error)}), 500

@app.route("/", methods=['GET'])
def  home():
    return jsonify({"message": "welcome to  flask api"}), 200

@app.route('/createuser', methods=['POST'])
def create_user():
    try:
        data  = request.get_json()
        user = UserCreate(**data)
        result = crud.create_user(user)
        return jsonify(result), 201 if "message" in result else 400
    except ValidationError as e:
        return jsonify({"error": "Validation error", "details": e.errors()}), 400
    
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(crud.get_users()), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    result =  crud.get_user_byid(user_id)
    return  (jsonify(result), 200) if "error" not in result else  (jsonify(result), 404)


@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        user = UserUpdate(**data)
        result = crud.update_user(user_id, user)
        return jsonify(result), 200 if "message" in result else 400
    except ValidationError as e:
        return jsonify({"error": "validation error", "details": e.errors()}), 400
    

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = crud.delete_user(user_id)
    return jsonify(result), 200 if "message" in result else 404


if __name__ ==  "__main__":
    app.run(debug=True, port=5000)