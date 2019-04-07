import jwt
from flask import Flask, request, jsonify

from decorators import login_check
from models import user

app = Flask(__name__)
secret_jwt = 'ultimate'


@app.route('/login', methods=['POST'])
def login():
    if 'username' not in request.json or 'password' not in request.json:
        return jsonify({'message': 'Missing attribute'}), 400

    if request.json['username'] != 'admin' or request.json['password'] != 'admin':
        return jsonify({'message': 'Forbidden'}), 401

    encoded_jwt = jwt.encode({'username': request.json['username']}, secret_jwt, algorithm='HS256')
    encoded_jwt_str = encoded_jwt.decode('UTF-8')
    user['token'] = encoded_jwt_str

    response = jsonify({'message': 'Logged in'})
    response.set_cookie('token', encoded_jwt_str, httponly=True)

    return response


@app.route('/secret', methods=['GET'])
@login_check
def secret():
    return jsonify({'message': 'SECRET!'}), 200
