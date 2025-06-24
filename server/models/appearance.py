from . import db

class Appearance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    guest_id = db.Column(db.Integer, db.ForeignKey("guest.id"))
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.id"))

    guest = db.relationship("Guest", back_populates="appearances")
    episode = db.relationship("Episode", back_populates="appearances")
