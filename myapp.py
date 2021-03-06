import os
import re

from flask import Flask, request
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Items, Itemlist
from resources.store import Store, StoreList
# while importing any python program it runs it or check it in case of oop thus to control that we use __name__ == '__main__'
app = Flask(__name__)


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    uri, 'sqlite:///data.db')
# sqlite can be changed with any db like mysql etc
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# extention of flask Sqlalchemy tracker is turned off

app.config['PROPAGATE_EXCEPTIONS'] = True
# helpful for error propagation
api = Api(app)
app.secret_key = "Nilesh"


jwt = JWT(app, authenticate, identity)
# jwt makes a new point as /auth which takes username and password which then uses authenticate function which returns user and jwt token
# this jwt token is used by identity thus request is authenticated

items = []

# no need of jsonify as it can be done automatically by rest
# code 404 not found
# 200 resource get
# 201 resources posted
# 202 accepted
# 400 bad request

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Items, '/item/<string:name>')
api.add_resource(Itemlist, "/items")
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
# debug = True helps fo getting good error messages

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True)  # important to mention debug=True
