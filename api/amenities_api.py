from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import amenities_api, data_manager, api
from data.DataManager import EntityType
from model.amenity import Amenity

amenity_model = amenities_api.model('Amenity', {
    'name': fields.String(required=True, description='Amenity name')
})


@amenities_api.route("/")
class NewAmenity(Resource):
    @amenities_api.expect(amenity_model)
    @amenities_api.doc('create_amenity')
    def post(self):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        name = data.get('name')
        if not name:
            api.abort(400, message='Missing required field')

        amenities = data_manager.get_list(EntityType.AMENITY)
        for amenity in amenities:
            if amenity['name'] == name:
                api.abort(409, message='Amenity name already exists')

        new_amenity = Amenity(name)
        result = data_manager.save(new_amenity)
        return result, 201

    @amenities_api.doc('list of all amenities')
    def get(self):
        amenities = data_manager.get_list(EntityType.AMENITY)
        return amenities, 200


@amenities_api.route("/<string:amenity_id>")
class EditAmenity(Resource):
    @amenities_api.doc('get inform about an amenity')
    def get(self, amenity_id):
        result = data_manager.get(amenity_id, EntityType.AMENITY)
        if result is None:
            api.abort(404, message='Amenity not found')
        else:
            return result, 200

    @amenities_api.doc('update inform about an amenity')
    @amenities_api.expect(amenity_model)
    def put(self, amenity_id):
        if not request.json:
            api.abort(400, message='Invalid input')
        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')
        name = data.get('name')
        if not name:
            api.abort(400, message='Missing required field')

        amenity_to_update = data_manager.get(amenity_id, EntityType.AMENITY)
        if amenity_to_update is None:
            api.abort(404, message='Amenity not found')

        amenities = data_manager.get_list(EntityType.AMENITY)
        for amenity in amenities:
            if amenity['name'] == name and amenity['id'] != amenity_id:
                api.abort(409, message='Amenity name already exists')

        updated_amenity = Amenity(name)
        updated_amenity.id = amenity_id
        result = data_manager.update(updated_amenity)
        if result is None:
            api.abort(400, message='Failed to update amenity')
        return result, 200

    @amenities_api.doc('delete a specific amenity')
    def delete(self, amenity_id):
        result = data_manager.delete(amenity_id, EntityType.AMENITY)
        if result is None:
            api.abort(404, message='Amenity not found')
        else:
            return jsonify({"message": "deleted successfully"})