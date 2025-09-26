# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return jsonify({"message": "Welcome to User Management API!"})

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400

    user_id = len(users) + 1
    users[user_id] = {"id": user_id, "name": data["name"], "email": data["email"]}
    return jsonify(users[user_id]), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    users[user_id].update(data)
    return jsonify(users[user_id])

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    deleted_user = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted_user})

if __name__ == "__main__":
    app.run(debug=True)
