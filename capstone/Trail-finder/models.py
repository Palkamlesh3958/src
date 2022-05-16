"""Models for trail finder app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Users."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    confirm_password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Show user details when printed."""
        return f"""<User user_id={self.user_id} 
                    username={self.username} 
                    email={self.email}>"""


# class User(db.model):
#     """A user."""

#     __tablename__ = "users"

#     user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     email = db.Column(db.String, unique=True)
#     pasword = db.Column(db.String)

#     def __repr__(self):
#         return f<"User user_id={self.user_id} email={self.email}">


# def connect_to_db(flask_app, db_uri="postgresql:///trailfinder", echo=True):
#     flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
#     flask_app.config["SQLALCHEMY_ECHO"] = True
#     flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     db.app = flask_app
#     db.init_app(flask_app)

#     print("Connected to the db!")

def connect_to_db(app, db_name):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, "trailfinder")
