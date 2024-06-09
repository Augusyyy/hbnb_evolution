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

        commentor_user_id = data.get('commentor_user_id')
        feedback = data.get('feedback')
        rating = data.get('rating')

        if not (commentor_user_id and feedback and rating is not None):
            api.abort(400, message='Missing required field')

        if not (isinstance(rating, int) and 1 <= rating <= 5):
            api.abort(400, message='Invalid rating value')

        review_to_update = review_model.get(review_id, EntityType.REVIEW)
        if review_to_update is None:
            api.abort(404, message='Review not found')

        updated_review = Review(commentor_user_id, review_to_update['place_id'], feedback, rating)
        updated_review.id = review_id

        result = data_manager.update(updated_review)
        if result is None:
            api.abort(400, message='Failed to update review')
        return result, 200

    @reviews_api.doc('delete review')
    def delete(self, review_id):
        result = data_manager.delete(review_id, EntityType.REVIEW)
        if result is None:
            api.abort(404, message='Review not found')
        else:
            return jsonify({"message": "deleted successfully"})
