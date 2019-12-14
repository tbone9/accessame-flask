import models
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user

place = Blueprint('places', 'place')

@place.route('/', methods=['GET'])
def get_all_places():
    try:
        all_places = models.Place.select()
        all_places = [model_to_dict(place) for place in all_places]
        return jsonify(data=all_places, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

@place.route('/user/', methods=['GET'])
def get_user_places():
    print('place index route')
    try:
        this_users_places = models.Place.select().where(models.Place.user == current_user.id)

        this_users_places = [model_to_dict(place) for place in this_users_places]

        print(this_users_places)
        return jsonify(data=this_users_places, status={'code': 200, 'message': 'Success'})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Error getting the resources'})

@place.route('/<placeId>/',methods=['GET'])
def show_place(placeId):
    # if not current_user.is_authenticated: # Checks if user is logged in
    #     return jsonify(data={}, status={'code': 401, 'message': 'You must be logged in to view this place'})
    try:
        found_place = models.Place.get(id=placeId)
        place_dict = model_to_dict(found_place)
        
        return jsonify(data=place_dict,status={"code":"201","message":"place found"})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Place to show does not exist'})

@place.route('/', methods=['POST'])
def create_place():
    print('place create route')
    print('CURRENT USER', current_user)
    if not current_user.is_authenticated:
        print(current_user, 'NOT ALLOWED')
        return jsonify(data={}, status={'code': 401, 'message': 'You must be logged in to create a place'})
    # user = models.User.get_by_id(current_user.id)
    # user_dict = model_to_dict(user)
    # print(user_dict, 'User DICT')

    payload = request.get_json()
    payload['user'] = current_user.id
    created_place = models.Place.create(**payload)
    create_place_dict = model_to_dict(created_place)
    return jsonify(status={'code': 201, 'msg': 'success'}, data=create_place_dict)

@place.route('/<placeId>/', methods=['PUT'])
def update_place(placeId):
    print('place edit route')
    payload = request.get_json()
    if not current_user.is_authenticated:
        return jsonify(data={}, status={'code': 401, 'message':'You must be logged in to update place'})
    try:
        place = models.Place.get_by_id(placeId)
        place_dict = model_to_dict(place)
        print(place_dict, 'PLACE DICT')
        # if place_dict.user.id is not current_user.id: 
        #     return jsonify(data={}, status={'code': 401, 'message': 'You can only update your own places'})
        updated_place = models.Place.update(
                main_entrance=payload['main_entrance'],
                bathroom=payload['bathroom'],
                overall=payload['overall'],
            ).where(models.Place.id==placeId).execute()
        updated_place_dict = model_to_dict(models.Place.get(id=placeId))
        return jsonify(data=updated_place_dict, status={"code": 201, "message": "Place updated"})
    except models.DoesNotExist:
        return jsonify(data={}, status={'code': 401, 'message': 'Place to update does not exist'})

@place.route('/<placeId>/', methods=['DELETE'])
# @login_required
def delete_place(placeId):
    
    place_to_delete = models.Place.get_by_id(placeId)

    if place_to_delete.user.id != current_user.id:
        return jsonify(data="Forbidden", status={'code': 403, 'message': "User can only delete their own places."})
    else:
        place_name = place_to_delete.name
    # articles_to_delete = models.Article.select().where(models.Article.topic.user.id == current_user.id)
    
    # articles_to_delete.delete()
    place_to_delete.delete_instance(recursive=True)
    return jsonify(data='Place successfully deleted', status={"code": 200, "message": "{} deleted successfully".format(place_name)})