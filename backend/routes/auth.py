from flask import Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
import simplejson as json

from .base import *
from models.base import db
from models.user import User

auth = Blueprint('auth', __name__)

def authenticate(username, password):
    user = User.query.filter_by(username=username, password=password).first()
   
    if user:
        return user

def identity(payload):
    print(payload['identity'])
    return None

@auth.route('/user', methods=['POST'])
def createUser():
    message = "User created."

    try :
        userInfo = json.loads(request.data)

        user = User(username=userInfo['username'], password=userInfo['password'], email=userInfo['email'])

        db.session.add(user)
        db.session.commit()   

    except AssertionError as err:
        message = err.args[0]

        return returnResponse(400, err.args[0], None)

    except IntegrityError as err:
        message = "Server error"
        db.session.rollback()

        if "(sqlite3.IntegrityError) UNIQUE constraint failed:" in err.args[0]:
            message = "User already created"

        return returnResponse(500, message, None)

    return returnResponse(200, message, { "id": user.id})

@auth.route('/user/<int:id>', methods=['GET'])
def GetUserById(id):
    users = User.query.filter_by(id=id).first()
    
    return returnResponse(200, "User.", users)

@auth.route('/users', methods=['GET'])
def GetAllUsers():
    users = User.query.all()
    
    return returnResponse(200, "All users.", users)