from flask_sqlalchemy import SQLAlchemy

class Object:
    def __init__(self):
        self.message = ""
        self.data = None

    def reprJSON(self):
        return dict(message=self.message, data=self.data)

db = SQLAlchemy()