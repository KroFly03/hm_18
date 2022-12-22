import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.model.user import User
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        data['password'] = self.get_hash(data['password'])
        user = User(**data)
        return self.dao.create(user)

    def update(self, data):
        uid = data.get('id')

        user = self.get_one(uid)

        user.username = data.get('username')
        user.password = self.get_hash(data.get('password'))
        user.role = data.get('role')

        return self.dao.update(user)

    def delete(self, uid):
        user = self.get_one(uid)

        return self.dao.delete(user)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def compare_passwords(self, password_hash, user_password):
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            user_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
