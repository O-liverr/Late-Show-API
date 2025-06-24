from server.app import app
from server.models import db, Guest, Episode, Appearance

with app.app_context():
    db.drop_all()
    db.create_all()
    g1 = Guest(name="John Doe", occupation="Actor")
    e1 = Episode(date="2023-06-19", number=1)
    db.session.add(g1)
    db.session.add(e1)
    db.session.commit()
    a1 = Appearance(rating=5, guest_id=g1.id, episode_id=e1.id)
    db.session.add(a1)
    db.session.commit()
