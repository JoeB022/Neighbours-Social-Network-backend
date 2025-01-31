from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'
    
    event_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    location = db.Column(db.String(255), nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    organizer = db.relationship('User', backref=db.backref('events', lazy=True))
    
    def __repr__(self):
        return f'<Event {self.title}>'

class Post(db.Model):
    __tablename__ = 'posts'
    
    post_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    created_by_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    
    created_by = db.relationship('User', backref=db.backref('posts', lazy=True))
    
    def __repr__(self):
        return f'<Post {self.content[:20]}>'

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    neighborhood = db.Column(db.String(100))

    def __repr__(self):
        return f'<User {self.name}>'
    
    # Flask-Login required methods
    def get_id(self):
        return str(self.user_id)
