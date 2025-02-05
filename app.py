import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend and API interaction

# Load configurations from environment variables or use defaults
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
app.config['JWT_TOKEN_LOCATION'] = ['headers']
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'Bearer'

jwt = JWTManager(app)

# Initialize database and migration
from models import db, User  # Ensure db is imported from models
db.init_app(app)
migrate = Migrate(app, db)

# Import and register Blueprints
from routes.auth import auth_bp
from routes.event import event_bp
from routes.post import post_bp

app.register_blueprint(auth_bp)
app.register_blueprint(event_bp)
app.register_blueprint(post_bp)

# User Loader for Flask-Login
@app.route('/')
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Flask Application Route Documentation</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f6f9;
      color: #333;
    }

    header {
      background-color: #007bff;
      color: white;
      text-align: center;
      padding: 1rem 0;
    }

    header h1 {
      margin: 0;
    }

    .container {
      max-width: 1200px;
      margin: 20px auto;
      padding: 20px;
      background-color: white;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .route-section {
      margin-bottom: 20px;
    }

    .route-section h2 {
      font-size: 1.6rem;
      color: #007bff;
      margin-bottom: 10px;
    }

    .route-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }

    .route-table th, .route-table td {
      padding: 12px;
      border: 1px solid #ddd;
      text-align: left;
    }

    .route-table th {
      background-color: #f8f9fa;
      color: #007bff;
    }

    .route-table tr:nth-child(even) {
      background-color: #f9f9f9;
    }

    .route-table td {
      font-size: 0.95rem;
    }

    .flash-message {
      background-color: #d4edda;
      color: #155724;
      padding: 10px;
      border: 1px solid #c3e6cb;
      border-radius: 5px;
      margin-top: 10px;
    }

    .flash-danger {
      background-color: #f8d7da;
      color: #721c24;
      border-color: #f5c6cb;
    }

    .route-description {
      margin-top: 10px;
      font-size: 1rem;
    }

    .route-description p {
      line-height: 1.5;
    }
  </style>
</head>
<body>

  <header>
    <h1>Flask Application Route Documentation</h1>
  </header>

  <div class="container">
    <section class="route-section">
      <h2>1. Authentication Routes</h2>

      <table class="route-table">
        <thead>
          <tr>
            <th>Route</th>
            <th>Method(s)</th>
            <th>Action</th>
            <th>Flash Message</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>/login</td>
            <td>GET, POST</td>
            <td>
              <p class="route-description">The login page where users can authenticate themselves using their email and password.</p>
              <p class="route-description">POST Request: Tries to log in the user using the provided credentials.</p>
            </td>
            <td class="flash-message">
              Success: "Login successful!"<br>
              Failure: "Invalid credentials, please try again."
            </td>
          </tr>
          <tr>
            <td>/register</td>
            <td>GET, POST</td>
            <td>
              <p class="route-description">The registration page for new users to create an account.</p>
              <p class="route-description">POST Request: Registers a new user with the provided data and redirects to the login page.</p>
            </td>
            <td class="flash-message">"Account created successfully! You can log in now."</td>
          </tr>
          <tr>
            <td>/logout</td>
            <td>GET</td>
            <td>
              <p class="route-description">Logs out the currently logged-in user.</p>
              <p class="route-description">Action: Logs out the user and redirects to the login page.</p>
            </td>
            <td class="flash-message">"You have been logged out!"</td>
          </tr>
        </tbody>
      </table>
    </section>

    <section class="route-section">
      <h2>2. Event Routes</h2>

      <table class="route-table">
        <thead>
          <tr>
            <th>Route</th>
            <th>Method(s)</th>
            <th>Action</th>
            <th>Flash Message</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>/events</td>
            <td>GET, POST</td>
            <td>
              <p class="route-description">Create a new event or view the list of events.</p>
              <p class="route-description">POST Request: Creates a new event and associates it with the logged-in user as the organizer.</p>
            </td>
            <td class="flash-message">"Event created successfully!"</td>
          </tr>
          <tr>
            <td>/events/view</td>
            <td>GET</td>
            <td>
              <p class="route-description">Displays a list of all events in the system.</p>
              <p class="route-description">Action: Retrieves all events from the database and renders them on the events page.</p>
            </td>
            <td class="flash-message">N/A</td>
          </tr>
        </tbody>
      </table>
    </section>

    <section class="route-section">
      <h2>3. Post Routes</h2>

      <table class="route-table">
        <thead>
          <tr>
            <th>Route</th>
            <th>Method(s)</th>
            <th>Action</th>
            <th>Flash Message</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>/posts</td>
            <td>POST</td>
            <td>
              <p class="route-description">Allows users to create a new post.</p>
              <p class="route-description">POST Request: Creates a new post with the provided content, associated with the logged-in user.</p>
            </td>
            <td class="flash-message">"Post created successfully!"</td>
          </tr>
          <tr>
            <td>/posts/&lt;int:post_id&gt;/delete</td>
            <td>POST</td>
            <td>
              <p class="route-description">Allows users to delete their own posts.</p>
              <p class="route-description">POST Request: Deletes a post if the user is the creator of the post.</p>
            </td>
            <td class="flash-danger">
              Success: "Post deleted successfully!"<br>
              Failure: "You are not authorized to delete this post."
            </td>
          </tr>
        </tbody>
      </table>
    </section>

    <section class="route-section">
      <h2>4. Error Handling Routes</h2>

      <table class="route-table">
        <thead>
          <tr>
            <th>Route</th>
            <th>Method(s)</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>/404</td>
            <td>GET</td>
            <td>Displays a 404 error page when a route is not found.</td>
          </tr>
          <tr>
            <td>/500</td>
            <td>GET</td>
            <td>Displays a 500 error page for internal server errors.</td>
          </tr>
        </tbody>
      </table>
    </section>

  </div>
</body>
</html>

"""


# Running the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
