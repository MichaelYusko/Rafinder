from flask import jsonify
from flask_restful import Resource, abort, request

from models.user import User


class UserRegistrationResource(Resource):
    def post(self):
        name = request.json.get('name')
        password = request.json.get('password')
        if name or password is None:
            abort(400)
        user = User(name=name, password=password)
        user.hash_password(password)
        user.save()
        return jsonify({'name': name})
