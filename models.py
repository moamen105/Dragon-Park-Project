from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    column = db.Column(db.String(1), nullable=False)
    row = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(10), default='safe')
    last_maintenance_date = db.Column(db.DateTime)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'), nullable=False)
    event_type = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
