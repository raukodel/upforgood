from .base import db

def init_app(app):
    db.init_app(app)

    from .user import User

    with app.app_context():
        db.create_all()

    return