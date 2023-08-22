from .models import Users


def get_user_by_email(email):
    try:
        return Users.query.filter(Users.email == email).one()
    except:
        return None
