# import required libraries and modules
from marshmallow import Schema, fields
from setup_db import db


# creating class as inheritance of Model class, cols acc to UML
class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# creating Schema class as inheritance of Schema for serialization
class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
