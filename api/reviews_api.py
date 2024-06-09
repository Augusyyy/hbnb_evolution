from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import reviews_api, api, data_manager
from data.DataManager import DataManager, EntityType
from model.review import Review

review_model = reviews_api.model('Review', {
    'user_id': fields.String(required=True, description='Comment user id'),
    'place_id': fields.String(required=True, description='Place id'),
    'comment': fields.String(required=True, description='Comment'),
    'rating': fields.Float(required=True, description='Rating')
})


@reviews_api.route("/<string:review_id>")
class EditReview(Resource):
    @reviews_api.doc('inform about review')
    def get(self, review_id):
        review = data_manager.get(review_id, EntityType.REVIEW)
        if review is None:
            api.abort(404, message='Review not found')
        else:
            detailed_review = {
                'id': review['id'],
                'place_id': review['place_id'],
                'user_id': review['user_id'],
                'rating': review['rating'],
                'comment': review['comment'],
                'created_at': review['created_at'],
                'updated_at': review['updated_at']
            }
            return detailed_review, 200

    @reviews_api.doc('update review')
    @reviews_api.expect(review_model)
    def put(self, review_id):
        if not request.json:
            api.abort(400, message='Invalid input')

        data = request.get_json()
        if data is None:
            api.abort(400, message='Invalid input')

        user_id = data.get('user_id')
        comment = data.get('comment')
        rating = data.get('rating')

        if not (user_id and comment and rating is not None):
            api.abort(400, message='Missing required field')

        if not (isinstance(rating, (int, float)) and 1 <= rating <= 5):
            api.abort(400, message='Invalid rating value')

        review_to_update = data_manager.get(review_id, EntityType.REVIEW)
        if review_to_update is None:
            api.abort(404, message='Review not found')

        updated_review = Review(user_id, review_to_update['place_id'], comment, rating)
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