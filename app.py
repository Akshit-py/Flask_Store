import os

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items_list
from resources.store import Store, StoreList

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #this turns off flasks sql_alchemy_modification tracker bcz we already have the same thing in SQLAlchemy library so we dont need flask lib to do the same.
app.secret_key='aks'
api=Api(app)



jwt=JWT(app, authenticate, identity)

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') #https://127.0.0.1:5000/student/name
api.add_resource(Items_list, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__=='__main__':
    from db import db #we are importing here because of circular imports
    db.init_app(app)
    app.run(port=5000, debug=True)
