from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models import db, Appearance

appearance_bp = Blueprint("appearance_bp", __name__)

@appearance_bp.route("/", methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.json
    if not (1 <= data.get("rating", 0) <= 5): 
        return jsonify({"error": "Rating must be between 1 and 5"}), 400
    a = Appearance(rating=data["rating"], guest_id=data["guest_id"], episode_id=data["episode_id"])
    db.session.add(a)
    db.session.commit()
    return jsonify({"id": a.id, "rating": a.rating, "guest_id": a.guest_id, "episode_id": a.episode_id}), 201
