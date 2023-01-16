from flask import request, jsonify
import re
from services.user import create_user

import services.user as user_service

from services.auth import auth_user
import hashlib
from datetime import datetime, timezone
import secrets


def controller(app):
    route_api = '/api/v1/'


    @app.route(route_api + 'login', methods=['POST'])
    def login():
        username = request.json.get("username")
        password = request.json.get("password")

        if not re.match("^[a-zA-Z]{1,16}$", username):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        if not re.match("^[0-9]{6}$", password):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        auth = auth_user(username, password)
        if auth == 1:
            return jsonify({'msg': 'Auth Success'}), 200
        else:
            return jsonify({'msg': 'Auth Failure'}), 401

    @app.route(route_api + 'users', methods=['POST'])
    def create():
        username = request.json.get('username')
        password = request.json.get('password')

        if not re.match("^[a-zA-Z]{1,16}$", username):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        if not re.match("^[0-9]{6}$", password):
            response = jsonify({'msg': 'Bad parameters', 'status_code': '400'})
            return response, 400

        if user_service.verify_user_exist(username):
            response = jsonify({'msg': 'User exists, change username'})
            return response, 401

        salt = secrets.token_hex(8)
        password_hashed = hashlib.md5(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()

        user_new = {
            "username": username,
            "password": password_hashed,
            "salt": salt,
            "created_at": datetime.now(timezone.utc),
            "updated_at": datetime.now(timezone.utc),
        }
        r = create_user(user_new)
        return {'User created': f'{r}:yes'}
