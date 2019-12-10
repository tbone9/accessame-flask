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

@rating.route('/one/<ratingId>/', methods=['GET'])
def get_one_rating(ratingId):
    if not current_user.is_authenticated: # Checks if user is logged in
        return jsonify(data={}, status={'code': 401, 'message': 'You must be logged in to view this rating'}) 
    try:
        one_rating = models.Rating.get(id=ratingId)
        rating_dict = model_to_dict(one_rating)
        return jsonify(data=rating_dict,status={"code":"201","message":"Rating found"})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Rating to show does not exist'})

@rating.route('/user/<userId>/', methods=['GET'])
def get_user_ratings(userId):
    print('user ratings')
    try:
        this_users_ratings = models.Rating.select().where(models.Rating.user_id == current_user.id)

        this_users_ratings = [model_to_dict(rating) for rating in this_users_ratings]

        # this_users_ratings = [model_to_dict(rating) for rating in Models.Rating.select().where(models.Rating.user_id == current_user.id)]
        return jsonify(data=this_users_ratings, status={'code': 200, 'message': 'Success'})
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

@rating.route('/<ratingId>/', methods=['PUT'])
def update_rating(ratingId):
    payload = request.get_json()
    if not current_user.is_authenticated:
        return jsonify(data={}, status={'code': 401, 'message':'You must be logged in to update a rating'})
    try:
        rating = models.Rating.get_by_id(ratingId)
        rating_dict = model_to_dict(rating)
        print(rating_dict, 'RATING DICT')
        if rating_dict['user']['id'] is not current_user.id:
            return jsonify(data={}, status={'code': 401, 'message': 'You can only update your own ratings'})
        updated_rating = models.Rating.update(
                main_entrance=payload['main_entrance'],
                bathroom=payload['bathroom'],
                hallways=payload['hallways'],
                notes=payload['notes'],
            ).where(models.Rating.id == ratingId).execute()
        updated_rating_dict = model_to_dict(models.Rating.get(id=ratingId))
        return jsonify(data=updated_rating_dict, status={"code": 201, "message": "Rating updated"})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Rating to update does not exist'})

@rating.route('/<ratingId>/', methods=['DELETE'])
def delete_rating(ratingId):
    rating_to_delete = models.Rating.get_by_id(ratingId)
    if rating_to_delete.user.id != current_user.id:
        return jsonify(data="Forbidden", status={'code': 403, 'message': "User can only delete their own ratings."})
    
    rating_to_delete.delete_instance()
    return jsonify(data='Rating successfully deleted', status={"code": 200, "message": "Rating deleted successfully"})
