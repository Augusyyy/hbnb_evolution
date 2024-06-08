from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import cities_api
from data.DataManager import DataManager, EntityType
from model.city import City

city_model = cities_api.model('City', {
    'country_id': fields.String(required=True, description='Country id'),
    'name': fields.String(required=True, description='City name')
})

data_manager = DataManager()
citi_id_counter = 1


@cities_api.route("/")
class NewCity(Resource):
    @cities_api.expect(city_model)
    @cities_api.doc('creat new city')
    def post(self):
        json_data = request.get_json()
        name = json_data.get('name')
        country_id = json_data.get('country_id')

        if not name or not country_id:
            return jsonify('Missing required field'), 400

        countries = data_manager.get_list(EntityType.COUNTRY)
        country_exists = False
        for country in countries:
            if country['id'] == country_id:
                country_exists = True
                break

        if not country_exists:
            return {'message': 'Invalid country ID'}, 400

    @cities_api.doc('Retrieve all cities.')
    def get(self):
        cities = data_manager.get_list(EntityType.CITY)
        return cities, 200


@cities_api.route('/<string:country_id>')
class Cities(Resource):
    @cities_api.doc('Retrieve details of a specific city')
    def get(self, country_id):
        cities = data_manager.get_list(EntityType.CITY)
        for city in cities:
            if city['id'] == country_id:
                return city, 200
        return {'message': 'City not found'}, 404

    @cities_api.doc('Update an existing cities inform')
    @cities_api.expect(city_model)
    def put(self, city_id):
        json_data = request.get_json()

        name = json_data.get('name')
        country_id = json_data.get('country_id')

        if not name or not country_id:
            return jsonify('Missing required field'), 400

        countries = data_manager.get_list(EntityType.COUNTRY)

        country_exists = False
        for country in countries:
            if country['id'] == country_id:
                country_exists = True
                break

        if not country_exists:
            return {'message': 'Invalid country ID'}, 400

        cities = data_manager.get_list(EntityType.CITY)
        city_update = None

        for city in cities:
            if city['id'] == city_id:
                city_update = city
                break

        if city_update is None:
            return {'message': 'City not found'}, 404

        for city in cities:
            if city['name'] == name and city['country_id'] == country_id and city['id'] != country_id:
                return {'message': 'City name already exists in this country'}, 409

        city_update['name'] == name
        city_update['country_id'] = country_id
        city_update['updated_at'] = datetime.utcnow().isoformat()

        data_manager.update(city_update)
        return city_update, 200

    @cities_api.doc('Delete a specific city')
    def delete(self, city_id):
        cities = data_manager.get_list(EntityType.CITY)
        city_exists = False
        updated_cities = []

        for city in cities:
            if city['id'] == city_id:
                city_exists = True
            else:
                updated_cities.append(city)

        if city_exists:
            data_manager.update(updated_cities)
            return {'message': 'City deleted successfully'}, 200
        return {'message': 'City not found'}, 404
