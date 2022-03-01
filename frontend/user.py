from http import HTTPStatus
from flask import Flask, jsonify, request
from uuid import uuid4


user_storage = {
    "e7b3d405ac9a45758109f3daee0adfae": {
        "uid": "e7b3d405ac9a45758109f3daee0adfae", 
        "username": "ivanov",
    },
    "3074db5ea6064b75b5c8e13d0415a4e3": {
        "uid": "3074db5ea6064b75b5c8e13d0415a4e3", 
        "username": "petrov",
    },
}

app = Flask(__name__)

# create user
@app.post('/api/users/')
def add_user():
    try:
        user = request.json
    except (ValueError):
        return {"message": "user's data is incorrect"}, HTTPStatus.BAD_REQUEST
    user['uid'] = uuid4().hex
    user_storage[user['uid']] = user
    return user, HTTPStatus.CREATED

# get all users
@app.get('/api/users/')
def get_users():
    users = [user for _, user in user_storage.items()]
    return jsonify(users), HTTPStatus.OK

# get user by uid
@app.get('/api/users/<uid>')
def get_by_id(uid):
    user = user_storage.get(uid)
    if not user:
        return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
    return user, HTTPStatus.OK

# update user
@app.put('/api/users/<uid>')
def update_user(uid):
    if uid not in user_storage:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    try:
        user = request.json
    except (ValueError):
        return {"message": "user's data is incorrect"},  HTTPStatus.BAD_REQUEST
    user_storage[user['uid']] = user
    return user, HTTPStatus.OK

# delete user
@app.delete('/api/users/<uid>')
def delete_user(uid):
    if uid not in user_storage:
        return {"message": "user not found"}, HTTPStatus.NOT_FOUND
    user_storage.pop(uid)
    return {"message": "user was successfully deleted"}, HTTPStatus.NO_CONTENT
