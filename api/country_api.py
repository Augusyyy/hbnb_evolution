from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import country_api, data_manager, api
from data.DataManager import EntityType
from model.country import Country

country_model = country_api.model('Country', {
    'name': fields.String(required=True, description='Country name'),
    'code': fields.String(required=True, description='Country code')
})


@country_api.route("/")
class CountryList(Resource):
    @country_api.doc("get all countries")
    def get(self):
        countries = data_manager.get_list(EntityType.COUNTRY)
        if countries:
            return countries, 200
        api.abort(404, message='No countries found')


@country_api.route('/<string:country_code>')
class CountriesByCode(Resource):
    @country_api.doc('get_country')
    def get(self, country_code):
        countries = data_manager.get_list(EntityType.COUNTRY)
        for country in countries:
            if country['code'] == country_code:
                return country, 200
        return api.abort(404, message='Country not found')


@country_api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    @country_api.doc('get_country_cities')
    def get(self, country_code):
        all_countries = data_manager.get_list(EntityType.COUNTRY)

        country_found = None
        for country in all_countries:
            if country['code'] == country_code:
                country_found = country
                break

        if country_found is None:
            api.abort(404, message='Country not found')

        all_cities = data_manager.get_list(EntityType.COUNTRY)
        cities_in_country = []
        for city in all_cities:
            if city['country_id'] == country_found['id']:
                cities_in_country.append(city)

        if cities_in_country:
            return cities_in_country, 200
        else:
            api.abort(404, message='No cities found in this country')
