from app import db, ma

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.password = password

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'password')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
