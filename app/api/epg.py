# -*- coding: utf-8 -*-
"""
    api.users
    ~~~~~
    Handlers for user endpoint
"""
from flask import jsonify

from app.api import api_blueprint as api
from app import dbsession

# from ..models import User
from ..services import list_of_stations, list_of_stations_procedure, list_of_stations_name


@api.route('/')
def index():
    return list_of_stations()


@api.route('/procedure')
def procedure():
    return list_of_stations_procedure()

@api.route('station-name')
def station_name():
    return list_of_stations_name()

# @api.route('/users', methods=['GET'])
# def get_users():
#     """Returns list of users"""
#     result = dbsession.query(User).all()
#     if result is None:
#         return jsonify({'result': []})
#     return jsonify({'result': [r.to_dict() for r in result]})


@api.route('/users', methods=['POST'])
def create_user():
    """Creates a new user"""
    try:
        user = User(name='Robus', address='Shantinagar')
        dbsession.add(user)
        dbsession.commit()
        dbsession.flush()
    except Exception as e:
        print(e)
        return jsonify({
            'error': 'Yup'
        })
    else:
        return jsonify({
            "status": "done"
        })
