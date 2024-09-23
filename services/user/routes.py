"""This module contains the routes related to users."""

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from services.user import user_db
from services.user import models


user_bp = Blueprint('user', __name__)

@user_bp.route('/user', methods=['PUT'])
def update_user():
    # Validate the request body
    try:
        data = models.UserUpdateRequest(**request.json)
    except ValidationError as e:
        return jsonify({"Status": "failure", "reason": "Body validation failed", "error": e.errors()}), 400
    
    # Update the user in the database
    try:
        user_db.update_user(data)
        return jsonify({"Status": "success", "reason": None}), 200
    except Exception as e:
        print("Error updating user:", e)
        return jsonify({"Status": "failure", "reason": "Database is not available"}), 500
