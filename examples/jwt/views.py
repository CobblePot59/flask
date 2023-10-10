from flask import request, session, jsonify
from app import app, jwt
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity

@app.route('/login', methods=['POST'])
def login():
    login = request.json['login']
    password = request.json['password']

    if login == 'admin' and password == 'admin':
        token = create_access_token(identity=login)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Bad login'}), 401

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify('Successfully access to protected url'), 200
