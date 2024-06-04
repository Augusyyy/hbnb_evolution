from datetime import datetime
from flask_restx import Resource, Api, fields
from flask import Flask, jsonify, request
from api import reviews_api
from data import review_data
from model.review import Review


review_model = api.model('Review', {
    'id': fields.String(required=True, description='Review id'),
    'comment_user_id': fields.String(required=True, description='comment user id'),
    'place_id': fields.String(required=True, description='place id'),
    'feedback': fields.String(required=True, description='feedback'),
    'rating': fields.Integer(required=True, description='rating')
})


@reviews_api.route("/<string:review_id>")
class EditReview(Resource):
    @reviews_api.doc('inform about review')
    def get(self, review_id):
        pass

    @reviews_api.doc('update review')
    def put(self, review_id):
        pass

    @reviews_api.doc('delete review')
    def delete(self, review_id):
        pass