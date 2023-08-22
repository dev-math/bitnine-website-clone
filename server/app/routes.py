from flask import jsonify
from app import app
from app import views


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Flask API"})


@app.route("/users", methods=["POST"])
def create_user():
    return views.create_user()
