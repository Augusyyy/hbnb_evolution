from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields

from data import user_data
from model.user import User

app = Flask(__name__)

api = Api(app, version='1.0', title='hbnb_evolution API', description='A hbnb_evolution project API')
user_api = api.namespace("users", description='User operation')

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
    def get(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass


if __name__ == '__main__':
    app.run()
