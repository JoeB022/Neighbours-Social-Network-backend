from datetime import datetime
from models import User, Event, Post, db
from flask import Flask
import os
import bcrypt  # Import bcrypt for password hashing

app = Flask(__name__)  # Creating Flask app

# Set the correct database path
base_dir = os.path.abspath(os.path.dirname(__file__))  # Directory of seed.py
db_path = os.path.join(base_dir, "instance", "db.sqlite3")  # Path to app.db in instance/
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

def seed_data():
    """Seed the database with initial data."""
    with app.app_context():
        # Drop all tables and recreate them for a fresh start
        db.drop_all()
        db.create_all()

        # Sample users (20 records)
        users_data = [
            {"name": "John Doe", "email": "john@example.com", "password": "password123", "neighborhood": "Sunnydale"},
            {"name": "Jane Smith", "email": "jane@example.com", "password": "password123", "neighborhood": "Riverside"},
            {"name": "Alice Brown", "email": "alice@example.com", "password": "password123", "neighborhood": "Lakeside"},
            {"name": "Bob Johnson", "email": "bob@example.com", "password": "password123", "neighborhood": "Greenwich"},
            {"name": "Charlie Davis", "email": "charlie@example.com", "password": "password123", "neighborhood": "Pinehill"},
            {"name": "Diana Wilson", "email": "diana@example.com", "password": "password123", "neighborhood": "Birchwood"},
            {"name": "Eva Martinez", "email": "eva@example.com", "password": "password123", "neighborhood": "Riverside"},
            {"name": "Frank White", "email": "frank@example.com", "password": "password123", "neighborhood": "Lakeview"},
            {"name": "Grace Lee", "email": "grace@example.com", "password": "password123", "neighborhood": "Parkway"},
            {"name": "Henry Harris", "email": "henry@example.com", "password": "password123", "neighborhood": "Sunset"},
            {"name": "Isla Thompson", "email": "isla@example.com", "password": "password123", "neighborhood": "Maplewood"},
            {"name": "Jack King", "email": "jack@example.com", "password": "password123", "neighborhood": "Cottonwood"},
            {"name": "Katherine Scott", "email": "katherine@example.com", "password": "password123", "neighborhood": "Hillcrest"},
            {"name": "Liam Clark", "email": "liam@example.com", "password": "password123", "neighborhood": "Sunnydale"},
            {"name": "Maya Rodriguez", "email": "maya@example.com", "password": "password123", "neighborhood": "Parkview"},
            {"name": "Nina Perez", "email": "nina@example.com", "password": "password123", "neighborhood": "Willowbrook"},
            {"name": "Oscar Martinez", "email": "oscar@example.com", "password": "password123", "neighborhood": "Greenfield"},
            {"name": "Paul Walker", "email": "paul@example.com", "password": "password123", "neighborhood": "Riverside"},
            {"name": "Quinn Robinson", "email": "quinn@example.com", "password": "password123", "neighborhood": "Riverside"},
            {"name": "Rebecca Lewis", "email": "rebecca@example.com", "password": "password123", "neighborhood": "Sunshine"},
        ]

        # Adding users to the database with hashed passwords
        for user in users_data:
            hashed_password = bcrypt.hashpw(user["password"].encode("utf-8"), bcrypt.gensalt())  # Hash password
            new_user = User(name=user["name"], email=user["email"], password=hashed_password.decode("utf-8"), neighborhood=user["neighborhood"])
            db.session.add(new_user)

        # Sample events (20 records)
        events_data = [
            {"title": "Community BBQ", "description": "Join us for a fun-filled BBQ with music and games!", "date": "2025-03-25", "location": "Sunnydale Park", "organizer_id": 1},
            {"title": "Neighborhood Clean-Up", "description": "Help us keep our neighborhood clean by joining our clean-up event.", "date": "2025-04-10", "location": "Riverside Street", "organizer_id": 2},
            {"title": "Farmers Market", "description": "Come shop for fresh local produce at the Riverside Farmers Market.", "date": "2025-04-12", "location": "Riverside Plaza", "organizer_id": 3},
            {"title": "Community Walk", "description": "A group walk through the park to promote fitness and wellness.", "date": "2025-05-01", "location": "Lakeside Park", "organizer_id": 4},
            {"title": "Summer Festival", "description": "Celebrate summer with music, food, and family fun!", "date": "2025-06-15", "location": "Lakeside Amphitheater", "organizer_id": 5},
            {"title": "Neighborhood Potluck", "description": "Bring your favorite dish and share with your neighbors!", "date": "2025-07-04", "location": "Greenwich Community Center", "organizer_id": 6},
        ]

        # Adding events to the database
        for event in events_data:
            new_event = Event(
                title=event["title"],
                description=event["description"],
                date=datetime.strptime(event["date"], "%Y-%m-%d"),
                location=event["location"],
                organizer_id=event["organizer_id"],
            )
            db.session.add(new_event)

        # Sample posts (20 records)
        posts_data = [
            {"content": "Looking forward to the Community BBQ this weekend! Who's coming?", "created_by_id": 1},
            {"content": "Don't forget to bring your sunscreen for the Summer Festival!", "created_by_id": 2},
            {"content": "Had a great time at the Spring Carnival today!", "created_by_id": 3},
            {"content": "Join us for the Holiday Tree Lighting ceremony this Friday!", "created_by_id": 4},
            {"content": "Anyone up for the Neighborhood Walk on Saturday morning?", "created_by_id": 5},
        ]

        # Adding posts to the database
        for post in posts_data:
            new_post = Post(content=post["content"], created_by_id=post["created_by_id"])
            db.session.add(new_post)

        # Commit all changes to the database
        db.session.commit()

        print("Data seeded successfully.")

# Run the seeding function
if __name__ == "__main__":
    seed_data()
