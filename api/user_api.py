from importlib.resources import Resource
from urllib import request

from flask import jsonify
from flask_restx import fields

from api import api, user_api, app
from data import user_data

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
        return jsonify(user_data['User'])

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

        for user in user_data['User']:
            if user['email'] == email:
                api.abort(409, message='Email already exists')

        new_user = User(email, password, first_name, last_name)

        user_data['User'].append({
            'id': new_user.id,
            'created_at': new_user.created_at.isoformat(),
            'updated_at': new_user.updated_at.isoformat(),
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email,
            'password': new_user.password
        })

        return_data = {
            'id': new_user.id,
            'created_at': new_user.created_at.isoformat(),
            'updated_at': new_user.updated_at.isoformat(),
            'first_name': new_user.first_name,
            'last_name': new_user.last_name,
            'email': new_user.email
        }

        return jsonify(return_data)

    
@user_api.route('/<string:user_id>')
class UserParam(Resource):
    @user_api.doc('create user by id')
    @user_api.response(404, 'User not found')
    def get(self, user_id):
        user_list = user_data['User']
        for user in user_list:
            if user['id'] == user_id:
                return jsonify(user)
        api.abort(404, message='User not found!')

    @user_api.doc('delete_user')
    @user_api.response(204, 'User deleted successfully')
    @user_api.response(404, 'User not found')
    def delete(self, user_id):
        user_list = user_data['User']
        user_to_delete = None

        for user in user_list:
            if user['id'] == user_id:
                user_to_delete = user
                break

        if user_to_delete is None:
            api.abort(404, message='User not found!')

        del user_list[user_to_delete]

        return jsonify({"message": "User deleted successfully"})

    @user_api.doc('update_user')
    @user_api.expect(user_model)
    @user_api.response(200, 'User updated successfully')
    @user_api.response(400, 'Invalid input')
    @user_api.response(404, 'User not found')
    @user_api.response(409, 'Email already exists')
    def put(self, user_id):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()

        if data is None:
            api.abort(400, message='Invalid input')

        user_modify = None
        user_list = user_data['User']
        for user in user_list:
            if user['id'] == user_id:
                user_modify = user
                break

        if user_modify is None:
            api.abort(404, message='User not found!')

        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        if first_name:
            user_modify['first_name'] = first_name
        if last_name:
            user_modify['last_name'] = last_name
        if email:
            user_modify['email'] = email
        if password:
            user_modify['password'] = password

        user_modify['updated_at'] = datetime.now()

        return jsonify(user_modify)


if __name__ == '__main__':
    app.run()
