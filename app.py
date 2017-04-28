from flask import Flask
from flask_restful import Api

from resources.user import UserRegistrationResource

app = Flask(__name__)
api = Api(app)


api.add_resource(UserRegistrationResource, '/api/users')
