from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import db, Zone, Event

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

DIGESTION_TIME_HOURS = 5

def process_nudls_event(zone_id, event_type, timestamp):
    zone = Zone.query.filter_by(id=zone_id).first()
    
    if event_type == 'carnivore_added':
        zone.status = 'unsafe'
        db.session.commit()

    elif event_type == 'meal_consumed':
        zone.status = 'safe'
        zone.last_maintenance_date = timestamp
        db.session.commit()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('frontend/index.html')

@app.route('/zones', methods=['GET'])
def get_zones():
    zones = Zone.query.all()
    zone_list = [{'id': zone.id, 'column': zone.column, 'row': zone.row, 'status': zone.status} for zone in zones]
    return jsonify({'zones': zone_list})

@app.route('/zones/<int:zone_id>', methods=['GET'])
def get_zone(zone_id):
    zone = Zone.query.get_or_404(zone_id)
    return jsonify({'id': zone.id, 'column': zone.column, 'row': zone.row, 'status': zone.status})

@app.route('/nudls-webhook', methods=['POST'])
def nudls_webhook():
    data = request.json

    zone_id = data['zone_id']
    event_type = data['event_type']
    timestamp = data['timestamp']

    process_nudls_event(zone_id, event_type, timestamp)

    zone = Zone.query.get_or_404(zone_id)
    return jsonify({'id': zone.id, 'column': zone.column, 'row': zone.row, 'status': zone.status})

if __name__ == '__main__':
    app.run(debug=True)
