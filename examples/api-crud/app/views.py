from flask import request, session, jsonify
from app import app, jwt, db
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from models import Users


@app.route('/login', methods=['POST'])
def login():
    login = request.json['login']
    password = request.json['password']

    if login == 'admin' and password == 'admin':
        token = create_access_token(identity=login)
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Bad login'}), 401

@app.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    users = Users.query.all()
    jusers = [{'email': user.email, 'username': user.username, 'password': user.password} for user in users]
    return jsonify(jusers), 200

@app.route('/users/<id>', methods=['GET'])
@jwt_required()
def get_user(id):
    user = Users.query.filter_by(id = id).first()
    juser = {'email': user.email, 'username': user.username, 'password': user.password}
    return jsonify(juser), 200

@app.route('/users', methods=['POST'])
@jwt_required()
def add_user():
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    new_user = Users(email = email, username = username, password = password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Successfully added'}), 200

@app.route('/users/<id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    user = Users.query.filter_by(id = id).first()

    email = request.json['email']
    username = request.json['username']
    password = request.json['password']

    user.username = username
    user.email = email
    user.password = password
    db.session.commit()
    return jsonify({'message': 'Successfully updated'}), 200

@app.route('/users/<id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    Users.query.filter_by(id = id).delete()
    db.session.commit()
    return jsonify({'message': 'Successfully deleted'}), 200