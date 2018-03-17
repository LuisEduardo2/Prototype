from flask_httpauth import HTTPBasicAuth
from flask import request, make_response, jsonify

auth = HTTPBasicAuth()

users = {
    'username' : 'password'
}


@auth.verify_password
def get_pw(username,password):
    if username in users:
        if password == users.get(username):
            return users.get(username)
    return False

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)