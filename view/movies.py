from flask_restx import Resource, Namespace
from flask import request

from dao.model.movie import MovieSchema
from decorators import auth_required, admin_required
from implemented import movie_service

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        try:
            args = request.args
            all_movies = movie_service.get_all(args)
            return movies_schema.dump(all_movies), 200
        except Exception:
            return "Not found", 404

    @admin_required
    def post(self):
        data = request.json
        movie_service.create(data)

        return "Movie created", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        try:
            movie = movie_service.get_one(mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return "Not found", 404

    @admin_required
    def put(self, mid):
        data = request.json
        movie_service.update(data)

        return "Movie updated", 204

    @admin_required
    def delete(self, mid):
        movie_service.delete(mid)

        return "Movie deleted", 204
