from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from .models import Users, user_schema

def create_user():
    email = request.json["email"]
    password = request.json["password"]

    user = get_user_by_email(email)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "User already exists"}), 400

    pass_hash = generate_password_hash(password)
    user = Users(email, pass_hash)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "User successfully registered", "data": result}), 201
    except:
        return jsonify({"message": "Unable to create"}), 500

def get_user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None
