from flask import Flask, jsonify, request, make_response, abort, Blueprint
from Auth.authentications import *

example = Blueprint('example',__name__)

data = [
    {
        'id':1,
        'fruit':'pineapple'
    },{
        'id':2,
        'fruit':'watermelon'
    },{
        'id':3,
        'fruit':'strawberry'
    } ]

'GET SPECIFIC VALUE'
@example.route('/todo/getall', methods=['GET'])
def get_values():
    return jsonify({'values': data}), 200


'GET ALL VALUES'
@example.route('/todo/getvalue/<int:id>', methods=['GET'])
def get_value(id):
    value = [value for value in data if value['id'] == id]
    if len(value) == 0:
        abort(404,'{"message":"values not found"}')
    return jsonify({'values': value}), 200


'CREATE A UNIQUE VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@example.route('/todo/insert', methods=['POST'])
@auth.login_required
def create_new_value():
    if not request.json or not 'fruit' in request.json:
        abort(404,'{"message":"values not found"}')
    newdata = {
        'id': data[-1]['id'] + 1,
        'fruit': request.json['fruit']
    }
    data.append(newdata)
    return jsonify({'values': newdata}), 201


'UPDATE A SPECIFIC VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@example.route('/todo/update/<int:id>', methods=['PUT'])
@auth.login_required
def update_values(id):
    if not request.json or not 'fruit' in request.json:
        abort(404,'{"message":"values not found"}')
    for index,value in enumerate(data):
        if value['id'] == id:
            data[index]['fruit'] = request.json['fruit']
            return jsonify(value), 200
    abort(404,'{"message":"values not found"}')


'DELETE A SPECIFIC VALUE, BASIC AUTHORIZATION (username and password) IS REQUIRED'
#username and password authentication is required
@example.route('/todo/delete/<int:id>', methods=['DELETE'])
@auth.login_required
def delete_value(id):
    for index,value in enumerate(data):
        if value['id'] == id:
            return jsonify(data.pop(id)), 200
    abort(404,'{"message":"values not found"}')


@example.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)