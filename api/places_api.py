from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import places_api, api, data_manager
from data.DataManager import DataManager, EntityType
from model.place import Place
from model.review import Review


review_model = places_api.model('Review', {
    'comment_user_id': fields.String(required=True, description='comment user id'),
    'place_id': fields.String(required=True, description='place id'),
    'feedback': fields.String(required=True, description='feedback'),
    'rating': fields.Float(required=True, description='rating')
})

place_model = places_api.model('Place', {
    'host_user_id': fields.String(required=True, description='Host user id'),
    'name': fields.String(required=True, description='Hotel name'),
    'city_id': fields.String(required=True, description='City id'),
    'description': fields.String(required=True, description='Hotel description'),
    'address': fields.String(required=True, description='Hotel address'),
    'latitude': fields.String(required=True, description='Latitude'),
    'longitude': fields.String(required=True, description='Longitude'),
    'number_of_rooms': fields.Integer(required=True, description='Number of rooms'),
    'bathrooms': fields.Integer(required=True, description='Number of bathrooms'),
    'price_per_night': fields.Integer(required=True, description='Price per night'),
    'max_guests': fields.Integer(required=True, description='Maximum guests')
})


@places_api.route("/")
class NewPlace(Resource):
    @places_api.expect(place_model)
    @places_api.doc('New place')
    def post(self):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        name = data.get('name')
        host_user_id = data.get('host_user_id')
        city_id = data.get('city_id')
        description = data.get('description')
        address = data.get('address')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        number_of_rooms = data.get('number_of_rooms')
        bathrooms = data.get('bathrooms')
        price_per_night = data.get('price_per_night')
        max_guests = data.get('max_guests')


        if not (name and host_user_id and city_id and description and address and latitude and longitude and number_of_rooms is not None and bathrooms is not None and price_per_night is not None and max_guests is not None):
            api.abort(400, message='Missing required field')

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            api.abort(400, message='Invalid geographical coordinates')

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            api.abort(400, message='Geographical coordinates out of bounds')

        if not (isinstance(number_of_rooms, int) and number_of_rooms >= 0):
            api.abort(400, message='Invalid number of rooms')
        if not (isinstance(bathrooms, int) and bathrooms >= 0):
            api.abort(400, message='Invalid number of bathrooms')
        if not (isinstance(max_guests, int) and max_guests >= 0):
            api.abort(400, message='Invalid guest capacity')

        try:
            price_per_night = float(price_per_night)
        except ValueError:
            api.abort(400, message='Invalid price per night')

        cities = data_manager.get_list(EntityType.CITY)
        if not any(city['id'] == city_id for city in cities):
            api.abort(400, message='Invalid city ID')

        places = data_manager.get_list(EntityType.PLACE)
        for place in places:
            if place['name'] == name:
                api.abort(409, message='Place name already exists')

        new_place = Place(host_user_id, city_id, name, description, address, latitude, longitude, number_of_rooms,
                          bathrooms, price_per_night, max_guests)
        result = data_manager.save(new_place)
        return result, 201

    @places_api.doc('list of all place')
    def get(self):
        places = data_manager.get_list(EntityType.PLACE)
        return places, 200


@places_api.route('/<string:place_id>')
class EditPlace(Resource):
    @places_api.doc('all information about a place')
    def get(self, place_id):
        result = data_manager.get(place_id, EntityType.PLACE)
        if result is None:
            api.abort(404, message='Place not found')
        else:
            return result, 200

    @places_api.expect(place_model)
    @places_api.doc('update a place')
    def put(self, place_id):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        name = data.get('name')
        host_user_id = data.get('host_user_id')
        city_id = data.get('city_id')
        description = data.get('description')
        address = data.get('address')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        number_of_rooms = data.get('number_of_rooms')
        bathrooms = data.get('bathrooms')
        price_per_night = data.get('price_per_night')
        max_guests = data.get('max_guests')

        if not (name and host_user_id and city_id and description and address and latitude and longitude and number_of_rooms is not None and bathrooms is not None and price_per_night is not None and max_guests is not None):
            api.abort(400, message='Missing required field')

        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            api.abort(400, message='Invalid geographical coordinates')

        if not (-90 <= latitude <= 90) or not (-180 <= longitude <= 180):
            api.abort(400, message='Geographical coordinates out of bounds')

        if not (isinstance(number_of_rooms, int) and number_of_rooms >= 0):
            api.abort(400, message='Invalid number of rooms')
        if not (isinstance(bathrooms, int) and bathrooms >= 0):
            api.abort(400, message='Invalid number of bathrooms')
        if not (isinstance(max_guests, int) and max_guests >= 0):
            api.abort(400, message='Invalid guest capacity')

        try:
            price_per_night = float(price_per_night)
        except ValueError:
            api.abort(400, message='Invalid price per night')

        cities = data_manager.get_list(EntityType.CITY)
        if not any(city['id'] == city_id for city in cities):
            api.abort(400, message='Invalid city ID')

        place_to_update = data_manager.get(place_id, EntityType.PLACE)
        if place_to_update is None:
            api.abort(404, message='Place not found')

        places = data_manager.get_list(EntityType.PLACE)
        for place in places:
            if place['name'] == name and place['id'] != place_id:
                api.abort(409, message='Place name already exists')

        updated_place = Place(host_user_id, city_id, name, description, address, latitude, longitude, number_of_rooms, bathrooms, price_per_night, max_guests)
        updated_place.id = place_id
        result = data_manager.update(updated_place)
        if result is None:
            api.abort(400, message='Failed to update place')
        return result, 200

    @places_api.doc('delete a place')
    def delete(self, place_id):
        result = data_manager.delete(place_id, EntityType.PLACE)
        if result is None:
            api.abort(404, message='Place not found')
        else:
            return {"message": "deleted successfully"}


@places_api.route('/<string:place_id>/reviews')
class PLaceReviews(Resource):
    @places_api.expect(review_model)
    @places_api.doc('new reviews for a place')
    def post(self, place_id):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        commentor_user_id = data.get('commentor_user_id')
        feedback = data.get('feedback')
        rating = data.get('rating')

        if not (commentor_user_id and feedback and rating is not None):
            api.abort(400, message='Missing required field')

        if not (isinstance(rating, int) and 0 <= rating <= 5):
            api.abort(400, message='Invalid rating value')

        place = data_manager.get(place_id, EntityType.PLACE)
        if place is None:
            api.abort(404, message='Place not found')

        new_review = Review(commentor_user_id, place_id, feedback, rating)
        result = data_manager.save(new_review)
        return result, 201

    @places_api.doc('get all reviews for a place')
    def get(self, place_id):
        place = data_manager.get(place_id, EntityType.PLACE)
        if place is None:
            api.abort(404, message='Place not found')

        reviews = data_manager.get_list(EntityType.REVIEW)
        place_reviews = [review for review in reviews if review['place_id'] == place_id]
        return place_reviews, 200
