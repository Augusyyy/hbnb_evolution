from datetime import datetime
from flask import request
from flask_restx import Resource
from flask import jsonify
from flask_restx import fields
from api import api, user_api
from model.user import User
from api import data_manager
from data.DataManager import EntityType

user_model = api.model('User', {
    'email': fields.String(required=True, description='Email address'),
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'password': fields.String(required=True, description='Password')
})


@user_api.route("")
class UserList(Resource):
    @user_api.doc("get all users")
    def get(self):
        return data_manager.get_list(EntityType.USER)

    @user_api.doc('create user')
    @user_api.expect(user_model)
    @user_api.response(201, 'User created successfully')
    @user_api.response(400, 'Invalid input')
    @user_api.response(409, 'Email already exists')
    def post(self):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()

        if data is None:
            api.abort(400, message='Invalid input')
        if 'email' not in data:
            api.abort(400, message='Invalid input')
        if 'password' not in data:
            api.abort(400, message='Invalid input')

        email = data['email']
        password = data['password']
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')

        user_list = data_manager.get_list(EntityType.USER)
        for user in user_list:
            if user['email'] == email:
                api.abort(409, message='Email already exists')

        new_user = User(email, password, first_name, last_name)

        result = data_manager.save(new_user)

        return result


@user_api.route('/<string:user_id>')
class UserParam(Resource):
    @user_api.doc('create user by id')
    @user_api.response(404, 'User not found')
    def get(self, user_id):
        result = data_manager.get(user_id, EntityType.USER)
        if result is None:
            api.abort(404, message='User not found')
        else:
            return result

    @user_api.doc('delete_user')
    @user_api.response(204, 'User deleted successfully')
    @user_api.response(404, 'User not found')
    def delete(self, user_id):
        result = data_manager.delete(user_id, EntityType.USER)
        if result is None:
            api.abort(404, message='User not found')
        else:
            return jsonify({"message": "User deleted successfully"})

    @user_api.doc('update_user')
    @user_api.expect(user_model)
    @user_api.response(200, 'User updated successfully')
    @user_api.response(400, 'Invalid input')
    @user_api.response(404, 'User not found')
    @user_api.response(409, 'Email already exists')
    def put(self, user_id):
        data = request.get_json()
        if request.get_json() is None:
            user_api.bort(400, "Invalid input")

        user_list = data_manager.get_list(EntityType.USER)
        for item in user_list:
            if item['email'] == data['email'] and user_id != item['id']:
                user_api.abort(409, 'Email already exists')

        u = User(data['first_name'], data['last_name'], data['email'], data['password'])
        u.id = user_id
        result = data_manager.update(u)
        if result is None:
            return user_api.abort(404, message='User not found')
        else:
            return result, 201


@user_api.route('/<string:user_id>/reviews')
class UserReview(Resource):
    @user_api.doc('all the reviews for a user')
    def get(self, user_id):
        user = data_manager.get(user_id, EntityType.USER)
        if user is None:
            api.abort(404, message='User not found')

        reviews = data_manager.get_list(EntityType.REVIEW)
        user_reviews = [review for review in reviews if review['user_id'] == user_id]
        return user_reviews, 200
