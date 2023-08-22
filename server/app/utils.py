import datetime
from functools import wraps
from app import app
from flask import request, jsonify
import jwt
from .models import Users


def get_user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None


def require_user_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            auth_header = request.headers.get("Authorization")
            token = auth_header.split(" ")[1]
        except:
            return (
                jsonify({"message": "Token is missing. Authentication required."}),
                401,
            )

        try:
            payload = jwt.decode(
                token,
                app.config["SECRET_KEY"],
                algorithms="HS256",
                options={"require": ["exp", "sub", "iat"]},
            )
            current_user = get_user_by_email(email=payload["sub"])
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired. Please log in again."}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid."}), 401
        except:
            return jsonify({"message": "Invalid credentials."}, 401)
        return f(current_user, *args, **kwargs)

    return decorated
