import calendar
import datetime
import hashlib

import jwt
from flask_restx import Resource, Namespace
from flask import request, abort

from constants import JWT_SECRET, JWT_ALGORITHM
from dao.model.user import User
from database import db
from implemented import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        data = request.json
        username = data.get("username", None)
        password = data.get("password", None)
        print(f"{username}  {password}")

        return auth_service.generate_tokens(username, password)

    def put(self):
        try:
            refresh_token = request.json.get('refresh_token')

            return auth_service.approve_refresh_token(refresh_token)
        except Exception:
            return 401
