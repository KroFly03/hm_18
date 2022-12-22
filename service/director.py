from dao.director import DirectorDAO
from dao.model.director import Director


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self):
        return self.dao.get_all()
    
    def create(self, data):
        director = Director(**data)
        return self.dao.create(director)

    def update(self, data):
        did = data.get('id')

        director = self.get_one(did)

        director.name = data.get('name')

        return self.dao.update(director)

    def delete(self, did):
        director = self.get_one(did)

        return self.dao.delete(director)
