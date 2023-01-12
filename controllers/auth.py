from flask import request, jsonify
import re
from services.user import get_users

def controller_endpoints(app):
    route_api='/api/v1/'

    @app.route(route_api,methods=["GET"])
    def home():
        users = get_users()
        return users

    @app.route(route_api+'login', methods=['POST'])
    def login():
        username = request.json.get("username")
        password = request.json.get("password")
        #Validating
        """if username == '' or password == '':
            response = jsonify({'msg':'Bad parameters', 'status_code': '400'})
            return response, 400"""
        if not re.match("^[a-zA-Z]{1,16}$", username):
            response = jsonify({'msg':'Bad parameters', 'status_code': '400'})
            return response, 400
        if not re.match("^[0-9]{6}$", password):
            response = jsonify({'msg':'Bad parameters', 'status_code': '400'})
            return response, 400

        #auth_user = check_db_user()


        return {'username': username , 'password': password}
