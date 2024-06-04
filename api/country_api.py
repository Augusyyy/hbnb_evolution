from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import country_api
from data import country_data
from model.country import Country

country_model = api.model('Country', {
    'id': fields.String(required=True, description='County id'),
    'name': fields.String(required=True, description='Country name'),
    'code': fields.String(required=True, description='Country code')
})


@country_api.route("/")
class CountryList(Resource):
    @country_api.doc("get all countries")
    def get(self):
        pass


@country_api.route('/<string:country_code>')
class CountriesByCode(Resource):
    @country_api.doc('get_country')
    def get(self, country_code):
        pass


@country_api.route('/<string:country_code>/cities')
class CountryCities(Resource):
    @country_api.doc('get_country_cities')
    def get(self, country_code):
        pass

