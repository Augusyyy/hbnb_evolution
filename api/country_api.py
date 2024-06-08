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
            return jsonify(countries), 200
        api.abort(404, message='No countries found')


@country_api.route('/<string:country_code>')
class CountriesByCode(Resource):
    @country_api.doc('get_country')
    def get(self, country_code):
        countries = data_manager.get_list(EntityType.COUNTRY)
        for country in countries:
            if country['code'] == country_code:
                return jsonify(country), 200
            else:
                return api.abort(404, message='Country not found')


@country_api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    @country_api.doc('get_country_cities')
    def get(self, country_code):
        pass

