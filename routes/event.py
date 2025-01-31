from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, Event
from datetime import datetime

event_bp = Blueprint('event', __name__)

@event_bp.route('/events/create', methods=['POST'])
@jwt_required()
def create_event():
    try:
        data = request.get_json()  # Extract JSON payload from request
        user_id = get_jwt_identity()  # Get logged-in user's ID from JWT token

        if not data:
            return jsonify({"error": "Invalid request data"}), 400
        
        # Extract data from the request
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')
        location = data.get('location')

        if not all([title, description, date, location]):
            return jsonify({"error": "All fields are required"}), 400

        # Create a new event instance
        new_event = Event(
            title=title, 
            description=description, 
            date=datetime.strptime(data['date'], "%Y-%m-%d"), 
            location=location, 
            organizer_id=user_id
        )
        
        db.session.add(new_event)
        db.session.commit()

        return jsonify({"message": "Event created successfully", "event_id": new_event.event_id}), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@event_bp.route('/events/view', methods=['GET'])
def view_events():
    events = Event.query.all()
    event_list = [
        {
            "id": event.event_id,
            "title": event.title,
            "description": event.description,
            "date": event.date,
            "location": event.location,
            "organizer_id": event.organizer_id
        } for event in events
    ]
    return jsonify(event_list), 200
