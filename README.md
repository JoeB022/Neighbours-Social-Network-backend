# Neighborhood Social Network
# Repository deployed links
Backend = https://neighbours-social-network-backend.onrender.com
Frontend = https://neighbours-social-network-frontend.vercel.app



## Overview
The **Neighborhood Social Network** is a web application designed to help neighbors connect, organize events, and foster community collaboration. The platform enables users to post events, RSVP, comment, send private messages, and participate in discussions.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Authentication**: Register and log in securely.
- **Event Management**: Create and manage neighborhood events.
- **RSVP System**: Attend and track event participation.
- **Community Posts**: Post discussions and announcements.
- **Commenting System**: Engage in discussions on event posts.
- **Private Messaging**: Send direct messages to other users.
- **Real-time Updates**: Get updates on neighborhood activities.

## Tech Stack
- **Frontend**: React.js, Tailwind CSS
- **Backend**: Flask (Python), Flask-RESTful, Flask-JWT-Extended, Flask-CORS
- **Database**: PostgreSQL / SQLite (for development)
- **Authentication**: Flask-Login, JWT

## Installation
Clone the repository:
```sh
 git clone https://github.com/JoeB022/neighborhood-social-network.git
 cd neighborhood-social-network
```

### Backend Setup
1. Navigate to the backend folder:
   ```sh
   cd Backend
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```sh
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```
5. Run the backend server:
   ```sh
   flask run
   ```

### Frontend Setup
1. Navigate to the frontend folder:
   ```sh
   cd ../Frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm start
   ```

## API Endpoints
| Endpoint               | Method | Description |
|------------------------|--------|-------------|
| `/register`           | POST   | Register a new user |
| `/login`              | POST   | User login |
| `/events`             | GET    | Get all events |
| `/events`             | POST   | Create a new event |
| `/events/<event_id>`  | GET    | Get event details |
| `/events/<event_id>/rsvp` | POST | RSVP for an event |
| `/posts`              | GET    | Get all community posts |
| `/posts`              | POST   | Create a new post |
| `/posts/<post_id>/comment` | POST | Add a comment to a post |
| `/messages`           | POST   | Send a private message |

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---
Made with ❤️ for community building!


