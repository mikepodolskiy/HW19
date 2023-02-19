# import required libraries and modules
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

# creating namespace
genre_ns = Namespace('genres')


# creating class based views using namespaces for all required endpoints
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        """
        getting all genres list using method get_all of GenreService class object
        using serialization with Schema class object
        :return: genres list
        """
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        """
        getting one genre dict using method get_one of GenreService class object
        using serialization with Schema class object
        :return: genre with required id - dict
        """
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
