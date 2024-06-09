from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import reviews_api, api
from data.DataManager import DataManager, EntityType
from model.review import Review


review_model = reviews_api.model ('Review', {
    'comment_user_id': fields.String(required=True, description='comment user id'),
    'place_id': fields.String(required=True, description='place id'),
    'feedback': fields.String(required=True, description='feedback'),
    'rating': fields.Integer(required=True, description='rating')
})

data_manager = DataManager()


@reviews_api.route("/<string:review_id>")
class EditReview(Resource):
    @reviews_api.doc('inform about review')
    def get(self, review_id):
        result = data_manager.get(review_id, EntityType.REVIEW)
        if result is None:
            api.abort(404, message='Review not found')
        else:
            return result, 200

    @reviews_api.doc('update review')
    @reviews_api.expect(review_model)
    def put(self, review_id):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        coment_user_id = data.get('comment_user_id')
        place_id = data.get('place_id')
        feedback = data.get('feedback')
        rating = data.get('rating')

        if not coment_user_id or not place_id or not feedback or rating is None:
            api.abort(400, message='Missing input')

        review_to_update = review_model.get(review_id, EntityType.REVIEW)
        if review_to_update is None:
            api.abort(404, message='Review not found')

        update_review = Review(coment_user_id, place_id, feedback, rating)
        update_review.id = review_id
        result = data_manager.update(update_review)

        if result is None:
            api.abort(404, message='Failed to update review')
        return result, 200

    @reviews_api.doc('delete review')
    def delete(self, review_id):
        result = data_manager.delete(review_id, EntityType.REVIEW)
        if result is None:
            api.abort(404, message='Review not found')
        else:
            return jsonify({"message": "deleted successfully"})
        