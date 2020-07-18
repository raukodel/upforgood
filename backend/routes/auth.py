from flask import Blueprint, render_template, request
from sqlalchemy.exc import IntegrityError
import simplejson as json

from .base import *
from models.base import *
from models.user import User
from models.user import UserSchema

auth = Blueprint('auth', __name__)

# @auth.route('/')
# def index():
#     return returnResponse(200, None)


# @auth.route('/auth', methods=['POST'])
# def login():
#     user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()

#     if user is None:
#         return render_template('login.html', error="Usuario ou sennha invalido!")

#     return render_template('login.html', userLogged=user)

def authenticate(username, password):
    user = User.query.filter_by(username=username, password=password).first()
    if user:
        return user

def identity(payload):
    print(payload['identity'])
    return None

@auth.route('/user', methods=['POST'])
def createUser():
    returnObj = Object()
    returnObj.message = "User created"

    try :
        userInfo = json.loads(request.data)

        user = User(username=userInfo['username'], password=userInfo['password'], email=userInfo['email'])

        db.session.add(user)
        db.session.commit()   

    except AssertionError as err:
        returnObj.message = err.args[0]
        
        return returnResponse(400, returnObj)

    except IntegrityError as err:
        db.session.rollback()
        
        returnObj.message = "Server error"

        if "(sqlite3.IntegrityError) UNIQUE constraint failed:" in err.args[0]:
            print("User already created")

        return returnResponse(500, returnObj)

    return returnResponse(200, returnObj)

@auth.route('/user', methods=['GET'])
def GetUsers():
    users = User.query.all()

    schema = UserSchema(many=True)
    result = schema.dumps(users)
    return returnResponse(200, result)

@auth.route('/auth/<string:username>', methods=['GET'])
def getExample(username):
    users = User.query.all()
    
    return render_template('login.html', users=users)