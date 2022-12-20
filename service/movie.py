from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, did):
        return self.dao.get_one(did)

    def get_all(self, args):
        director = args.get('director_id')
        genre = args.get('genre_id')
        year = args.get('year')

        if director is not None:
            return self.dao.get_one_by_director_id(director)
        if genre is not None:
            return self.dao.get_one_by_genre_id(genre)
        if year is not None:
            return self.dao.get_one_by_year(year)
        else:
            return self.dao.get_all()

    def create(self, data):
        movie = Movie(**data)
        return self.dao.create(movie)

    def update(self, data):
        mid = data.get('id')

        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        return self.dao.update(movie)

    def delete(self, mid):
        movie = self.get_one(mid)

        return self.dao.delete(movie)
