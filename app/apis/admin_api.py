from traceback import print_exc
from flask import request, jsonify
from ..models.user_model import UserModel


def create_user():
    try:
        user_model = UserModel()
        user = request.get_json()["name"]
        created = user_model.create_user(user)
        if not created:
            return jsonify({"message": "User not created"}), 400
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def edit_user(name):
    try:
        print(name)
        user_model = UserModel()
        new_name = request.get_json()["newName"]
        edited = user_model.update_user(name, new_name)
        if not edited:
            return jsonify({"message": "User not edited"}), 400
        return jsonify({"message": "User edited"}), 201
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def delete_user(name):
    try:
        user_model = UserModel()
        deleted = user_model.delete_user(name)
        if not deleted:
            return jsonify({"message": "User not deleted"}), 400
        return jsonify({"message": "User deleted"}), 201
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500


def change_admin_password():
    try:
        user_model = UserModel()
        data = request.get_json()
        print(data["old_password"], data["new_password"])
        updated = user_model.change_admin_password(
            data["old_password"], data["new_password"])
        if not updated:
            return jsonify({"message": "Password not updated"}), 400
        return jsonify({"message": "Password updated"}), 201
    except Exception as e:
        print_exc()
        return jsonify({"message": "Something went wrong"}), 500
