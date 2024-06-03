from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)

api = Api(app, version='1.0', title='hbnb_evolution API', description='A hbnb_evolution project API')


@api.route('/users')
class UserList(Resource):
    def get(self):
        pass

    def post(self):
        pass


@api.route('/users/<string:user_id>')
class UserParam(Resource):
    def get(self, user_id):
        pass

    def delete(self, user_id):
        pass

    def put(self, user_id):
        pass
    

if __name__ == '__main__':
    app.run()
