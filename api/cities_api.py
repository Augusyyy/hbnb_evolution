from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request

import data
from api import cities_api, api
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
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        name = data.get('name')
        country_id = data.get('country_id')

        if not name or not country_id:
            api.abort(400, message='Missing required field')

        countries = data_manager.get_list(EntityType.COUNTRY)
        country_exists = False
        for country in countries:
            if country['id'] == country_id:
                country_exists = True
                break

        if not country_exists:
            api.abort(400, message='Missing required field')

        cities = data_manager.get_list(EntityType.CITY)
        for city in cities:
            if city['name'] == name and city['country_id'] == country_id:
                api.abort(400, message='Missing required field')

        new_city = City(name, country_id)
        result = data_manager.save(new_city)
        return result, 201

    @cities_api.doc('Retrieve all cities.')
    def get(self):
        cities = data_manager.get_list(EntityType.CITY)
        return cities, 200


@cities_api.route('/<string:city_id>')
class Cities(Resource):
    @cities_api.doc('Retrieve details of a specific city')
    def get(self, city_id):
        cities = data_manager.get_list(EntityType.CITY)
        for city in cities:
            if city['id'] == city_id:
                return city, 200
        api.abort(400, message='Missing required field')

    @cities_api.doc('Update an existing cities inform')
    @cities_api.expect(city_model)
    def put(self, city_id):
        json_data = request.get_json()
        name = json_data.get('name')
        country_id = json_data.get('country_id')

        if not name or not country_id:
            api.abort(400, message='Invalid input')

        countries = data_manager.get_list(EntityType.COUNTRY)

        country_exists = False
        for country in countries:
            if country['id'] == country_id:
                country_exists = True
                break

        if not country_exists:
            api.abort(400, message='Invalid country ID')

        cities = data_manager.get_list(EntityType.CITY)
        city_update = None

        for city in cities:
            if city['id'] == city_id:
                city_update = city
                break

        if city_update is None:
            api.abort(400, message='City not found')

        for city in cities:
            if city['name'] == name and city['country_id'] == country_id and city['id'] != country_id:
                api.abort(409, message='City name already exists in this country')

        updated_city = City(name, country_id)
        updated_city.id = city_id
        result = data_manager.update(updated_city)
        if result is None:
            api.abort(400, message='Failed to update city')
        return result, 200

    @cities_api.doc('Delete a specific city')
    def delete(self, city_id):
        result = data_manager.delete(city_id, EntityType.CITY)
        if result is None:
            api.abort(404, message='User not found')
        else:
            return {"message": "deleted successfully"}
