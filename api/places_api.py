from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import places_api
from model.place import Place

place_model = places_api.model('Place', {
    'host_user_id': fields.String(required=True, description='Host user id'),
    'name': fields.String(required=True, description='Hotel name'),
    'city_id': fields.String(required=True, description='City id'),
    'description': fields.String(required=True, description='Hotel description'),
    'address': fields.String(required=True, description='Hotel address'),
    'latitude': fields.String(required=True, description='Latitude'),
    'longitude': fields.String(required=True, description='Longitude'),
    'number_of_rooms' : fields.Integer(required=True, description='Number of rooms'),
    'bathrooms' : fields.Integer(required=True, description='Number of bathrooms'),
    'price_per_night' : fields.Integer(required=True, description='Price per night'),
    'max_guests' : fields.Integer(required=True, description='Maximum guests')
})


@places_api.route("/")
class NewPlace(Resource):
    @places_api.expect(place_model)
    @places_api.doc('New place')
    def post(self):
        pass

    @places_api.doc('list of all place')
    def get(self):
        pass


@places_api.route('/<string:place_id>')
class EditPlace(Resource):
    @places_api.doc('all information about a place')
    def get(self, place_id):
        pass

    @places_api.expect(place_model)
    @places_api.doc('update a place')
    def put(self, place_id):
        pass

    @places_api.doc('delete a place')
    def delete(self, place_id):
        pass


@places_api.route('/<string:place_id>/reviews')
class PLaceReviews(Resource):
    @places_api.expect(place_model)
    @places_api.doc('new reviews for a place')
    def post(self, place_id):
        pass

    @places_api.doc('get all reviews for a place')
    def get(self, place_id):
        pass
