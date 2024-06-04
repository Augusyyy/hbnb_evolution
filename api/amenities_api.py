from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import api, amenities_api
from data import amenity_data
from model.amenity import Amenity

amenity_model = api.model('Amenity', {
    'id': fields.String(required=True, description='Amenity id'),
    'name': fields.String(required=True, description='Amenity name')
})


@amenities_api.route("/")
class NewAmenity(Resource):
    @amenities_api.doc('create_amenity')
    def post(self):
        pass

    @amenities_api.doc('list of all amenities')
    def get(self):
        pass


@amenities_api.route("/<string:amenity_id>")
class EditAmenity(Resource):
    @amenities_api.doc('get inform about an amenity')
    def get(self, amenity_id):
        pass

    @amenities_api.doc('update inform about an amenity')
    def put(self, amenity_id):
        pass

    @amenities_api.doc('delete a specific amenity')
    def delete(self, amenity_id):
        pass