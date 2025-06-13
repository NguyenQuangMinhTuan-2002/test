from flask import Blueprint, jsonify
from services.user_service import get_all_users

user_bp = Blueprint("user", __name__)

@user_bp.route("/api/users", methods=["GET"])
def get_users():
    users = get_all_users()
    return jsonify([user.to_dict() for user in users])
