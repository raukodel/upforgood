from .auth import auth, authenticate, identity
from flask_jwt import JWT, jwt_required, current_identity

jwt = None

def init_app(app):
    app.register_blueprint(auth)

    jwt = JWT(app,  authenticate, identity)