from dao.genre import GenreDAO
from dao.model.genre import Genre


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        return self.dao.get_one(gid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        genre = Genre(**data)
        return self.dao.create(genre)

    def update(self, data):
        gid = data.get('id')

        genre = self.get_one(gid)

        genre.name = data.get('name')

        return self.dao.update(genre)

    def delete(self, gid):
        genre = self.get_one(gid)

        return self.dao.delete(genre)
