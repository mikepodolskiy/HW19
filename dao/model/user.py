# import required libraries and modules
from marshmallow import Schema, fields
from setup_db import db


# creating class as inheritance of Model class, cols acc to UML
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)  # unique parameter provision, user with same name will not be
    # created
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))


# creating Schema class as inheritance of Schema for serialization
class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()
    role = fields.Str()
