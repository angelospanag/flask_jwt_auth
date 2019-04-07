from functools import wraps
from http import HTTPStatus

from flask import request, jsonify

from models import user


def login_check(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({'message': 'Forbidden'}), HTTPStatus.FORBIDDEN

        if request.headers['Authorization'] != f'Bearer {user["token"]}':
            return jsonify({'message': 'Forbidden'}), HTTPStatus.FORBIDDEN

        return f(*args, **kwargs)

    return decorated
