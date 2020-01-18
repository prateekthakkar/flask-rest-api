from flask import Flask
from flask_restful import Api		
from flask_jwt import JWT,jwt_required

from security import authenticate,identity
from user import UserRegister

from items import *
	
app = Flask(__name__)
app.secret_key = "mysupersecretkey"
api = Api(app)

jwt = JWT(app, authenticate,identity) # Her JWT Create New Endpoint Like Auth For Authentication


api.add_resource(Item,'/item/<string:name>') #it look like http://127.0.0.1:5000/item/hello

api.add_resource(ItemList,'/items') #it look like http://127.0.0.0.1:5000/items

api.add_resource(UserRegister, '/register') #it look like http://127.0.0.1:5000/register

if __name__ == "__main__":
	app.run(port=5000,debug=True)
