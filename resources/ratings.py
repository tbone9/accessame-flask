import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

rating = Blueprint('ratings', 'rating')

@rating.route('/<placeId>/', methods=['GET'])
def get_place_ratings(placeId):
    print('place ratings')
    try:
        this_places_ratings = [model_to_dict(rating) for rating in models.Rating.select().where(models.Rating.place_id == placeId)]
        return jsonify(data=this_places_ratings, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

@rating.route('/<placeId>/', methods=['POST'])
def create_rating(placeId):
    print('create rating')
    if not current_user.is_authenticated:
        print(current_user, 'NOT ALLOWED')
        return jsonify(data={}, status={'code': 401, 'message': 'You must be logged in to create a rating'})
    place = models.Place.get_by_id(placeId)
    place_dict = model_to_dict(place)
    # username = models.User.get_by_id(current_user)
    payload = request.get_json()
    payload['place'] = placeId
    payload['user'] = current_user.id
    created_rating = models.Rating.create(**payload)
    create_rating_dict = model_to_dict(created_rating)
    return jsonify(status={'code': 201, 'msg': 'success'}, data=create_rating_dict)