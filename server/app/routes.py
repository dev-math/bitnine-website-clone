from flask import jsonify
from app import app
from app import views
from .utils import require_user_login


@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Flask API"})


@app.route("/users", methods=["POST"])
def create_user():
    return views.create_user()

@app.route("/login", methods=["POST"])
def login_user():
    return views.login_user()

@app.route("/secret", methods=["GET"])
@require_user_login
def secret(current_user):
    return jsonify({"message": "foo"})
