# import required libraries and modules
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

# creating namespace
director_ns = Namespace('directors')


# creating class based views using namespaces for all required endpoints
@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        """
        getting all directors list using method get_all of DirectorService class object
        using serialization with Schema class object
        :return: directors list
        """
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)
        return res, 200


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    def get(self, rid):
        """
        getting one director dict using method get_one of DirectorService class object
        using serialization with Schema class object
        :return: director with required id - dict
        """
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
