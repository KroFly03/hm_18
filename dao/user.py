from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(User).get(mid)

    def get_all(self):
        return self.session.query(User).all()

    def create(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def update(self, user):
        self.session.add(user)
        self.session.commit()

        return user

    def delete(self, user):
        self.session.delete(user)
        self.session.commit()

        return user

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()




