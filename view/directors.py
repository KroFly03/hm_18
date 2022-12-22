from flask_restx import Resource, Namespace
from flask import request
from dao.model.director import DirectorSchema
from decorators import auth_required, admin_required
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        data = request.json
        director_service.create(data)

        return "Director created", 201


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    @auth_required
    def get(self, did):
        try:
            director = director_service.get_one(did)
            return director_schema.dump(director), 200
        except Exception:
            return "Not found", 404

    @admin_required
    def put(self, did):
        data = request.json
        director_service.update(data)

        return "Director updated", 204

    @admin_required
    def delete(self, did):
        director_service.delete(did)

        return "Director deleted", 204
