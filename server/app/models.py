from app import db, ma, bcrypt, app


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()


class UsersSchema(ma.Schema):
    class Meta:
        fields = ("id", "email")


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
