from .base import db
from marshmallow import Schema, fields
from sqlalchemy.orm import validates

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    __usernameLength = 0
    __passwordLength = 0

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.__usernameLength = 3
        self.__passwordLength = 3

    def __repr__(self):
        return '<User %r>' % self.username

    def reprJSON(self):
        return dict(username=self.username, password=self.password, email=self.email)

    @validates('username')
    def validate_username(self, key, username):
        assert len(username) > self.__usernameLength, "Username needs to have more then %d letters" % (self.__usernameLength)
        
        return username

    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > self.__passwordLength, "Password needs to have more then %d characters" % (self.__passwordLength)
        
        return password

    @validates('email')
    def validate_email(self, key, email):
        assert '@' in email , "Email incorrect"
        
        return email

class UserSchema(Schema):
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()