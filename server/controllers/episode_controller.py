from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models import db, Episode

episode_bp = Blueprint("episode_bp", __name__)

@episode_bp.route("/", methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{"id": e.id, "date": e.date, "number": e.number} for e in episodes])

@episode_bp.route("/<int:id>", methods=["GET"])
def get_episode(id):
    e = Episode.query.get(id)
    if not e:
        return jsonify({"error": "Not Found"}), 404
    return jsonify({
        "id": e.id,
        "date": e.date,
        "number": e.number,
        "appearances": [{"id": a.id, "rating": a.rating, "guest_id": a.guest_id} for a in e.appearances]
    })

@episode_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    e = Episode.query.get(id)
    if not e:
        return jsonify({"error": "Not Found"}), 404
    db.session.delete(e)
    db.session.commit()
    return "", 204
