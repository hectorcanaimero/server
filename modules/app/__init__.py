''' flask app with mongo '''
import os
import json
import datetime
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_jwt_extended import JWTManager


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get('DB')
app.config['JWT_SECRET_KEY'] = os.environ.get('SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=1)
mongo = PyMongo(app)

flask_bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.json_encoder = JSONEncoder


from app.controllers import *