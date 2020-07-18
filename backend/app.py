from flask import Flask
from flask_cors import CORS
from flask import json
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


def create_app():
    import models, routes, services, database

    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICARIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/upforgoodDB.sqlite3'
    app.config['SECRET_KEY'] = 'super-secret'
    CORS(app)
    #cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    database.init_app(app)

    if __name__ == "__main__":
        app.run(debug=True)

    return app