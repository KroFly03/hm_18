from flask_restx import Resource, Namespace
from flask import request

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_genres = user_service.get_all()
        return users_schema.dump(all_genres), 200


    def post(self):
        data = request.json
        user_service.create(data)

        return "User created", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        try:
            user = user_service.get_one(uid)
            return user_schema.dump(user), 200
        except Exception:
            return "Not found", 404

    def put(self, uid):
        data = request.json
        user_service.update(data)

        return "User updated", 204

    def delete(self, uid):
        user_service.delete(uid)

        return "User deleted", 204
