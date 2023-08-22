import datetime
from app import db, bcrypt, app
from flask import request, jsonify
from .models import Users, user_schema
from .utils import get_user_by_email


def create_user():
    email = request.json["email"]
    password = request.json["password"]

    user = get_user_by_email(email)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "User already exists"}), 400

    user = Users(email, password)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "User successfully registered", "data": result}), 201
    except:
        return jsonify({"message": "Unable to create"}), 500
