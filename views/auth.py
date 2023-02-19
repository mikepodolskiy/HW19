# import required libraries and modules
import jwt
from flask import request
from flask_restx import Resource, Namespace, abort
from implemented import user_service
from constants import auth_secret as secret, algo
from service.auth import check_request_integrity, check_user_exist, compare_passwords, generate_access_token, \
    generate_refresh_token

# creating namespace
auth_ns = Namespace('auth')


# creating class based views using namespaces for all required endpoints
@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        username = req_json.get('username', None)
        password = req_json.get('password', None)
        filters = {'username': username,
                   'password': password
                   }
        # check if data is existing, otherwise abort
        if check_request_integrity([username, password]):
            abort(400)

        # get user by username from db, check if user exists, otherwise return error
        user = user_service.get_one_by_key(filters)
        if check_user_exist(user):
            return {"error": "Неверные учётные данные"}, 401

        # hash user password from request
        password_hash = user_service.get_hash(password)

        # check password correctness, otherwise return error
        if compare_passwords(password_hash, user.password):
            return {"error": "Неверные учётные данные"}, 401

        # generating tokens
        data = {
            'username': user.username,
            'role': user.role,
        }
        access_token = generate_access_token(data)
        refresh_token = generate_refresh_token(data)

        return {'access_token': access_token, 'refresh_token': refresh_token}, 201

    def put(self):
        req_json = request.json
        refresh_token = req_json.get('refresh_token', None)
        if user_service.check_request_integrity([refresh_token]):
            abort(400)
        try:
            data = jwt.decode(jwt=refresh_token, key=secret, algorithms=[algo])
        except Exception as e:
            abort(400)
        username = data.get('username')
        filters = {'username': username}
        # get user by username from db, check if user exists, otherwise return error
        user = user_service.get_one_by_key(filters)

        # generating tokens
        data = {
            'username': user.username,
            'role': user.role,
        }
        access_token = user_service.generate_access_token(data)
        refresh_token = user_service.generate_refresh_token(data)

        return {'access_token': access_token, 'refresh_token': refresh_token}, 201
