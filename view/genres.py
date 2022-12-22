from flask_restx import Resource, Namespace
from flask import request
from dao.model.genre import GenreSchema
from decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200

    @admin_required
    def post(self):
        data = request.json
        genre_service.create(data)

        return "Genre created", 201


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    @auth_required
    def get(self, gid):
        try:
            genre = genre_service.get_one(gid)
            return genre_schema.dump(genre), 200
        except Exception:
            return "Not found", 404

    @admin_required
    def put(self, gid):
        data = request.json
        genre_service.update(data)

        return "Genre updated", 204

    @admin_required
    def delete(self, gid):
        genre_service.delete(gid)

        return "Genre deleted", 204