# CodeTech - Interactive Learning Platform

CodeTech is a comprehensive learning platform designed to enhance theoretical knowledge acquisition for technical students. The platform offers interactive quizzes across various subjects, helping users build strong foundations in programming and related fields.

## Table of Contents

- [Project Overview](#project-overview)
- [Frontend](#frontend)
  - [Structure](#frontend-structure)
  - [Features](#frontend-features)
- [Backend](#backend)
  - [Structure](#backend-structure)
  - [API Endpoints](#api-endpoints)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

CodeTech is built as a full-stack application with a modern frontend and a robust backend. The platform allows users to:

- Register and log in to their accounts
- Access interactive quizzes on various technical subjects
- Track their progress and performance
- Compete with peers on leaderboards
- Receive instant feedback on quiz performance

## Frontend

### Structure

The frontend is built using Next.js, a popular React framework. The main components and pages include:

- `app/page.tsx`: The main homepage with subject previews
- `app/login/page.tsx`: User login page
- `app/signup/page.tsx`: User registration page
- `app/dashboard/page.tsx`: User dashboard showing progress
- `app/leaderboard/page.tsx`: Leaderboard page
- `app/subject/[id]/page.tsx`: Subject-specific page
- `app/quiz/[subjectId]/[levelId]/page.tsx`: Quiz page for a specific level
- `app/quiz/[subjectId]/[levelId]/[quizId]/page.tsx`: Individual quiz page

### Features

- Responsive design with a modern UI
- User authentication and authorization
- Interactive quiz interface
- Progress tracking and visualization
- Leaderboard functionality
- Subject-specific learning paths

## Backend

### Structure

The backend is built using FastAPI, a modern web framework for Python. The main components include:

- `backend/main.py`: Main FastAPI application with all endpoints
- `backend/init_db.py`: Database initialization script
- `backend/clear_db.py`: Database clearing script
- `backend/seed_main.py`: Database seeding script
- `backend/test_api.py`: API testing script

### API Endpoints

The backend provides a comprehensive REST API with the following key endpoints:

- **Authentication**
  - `POST /signup`: User registration
  - `POST /login`: User login
  - `GET /me`: Get current user info

- **Quiz Management**
  - `GET /quiz/{subject_id}/{level_id}`: Get quiz for a specific subject and level
  - `POST /quiz/{subject_id}/{level_id}/submit`: Submit quiz answers

- **Progress Tracking**
  - `GET /user/subjects`: Get user's subjects with progress
  - `POST /user/subjects/{subject_id}/levels/{level_id}/complete`: Mark a level as completed

- **Leaderboard**
  - `GET /leaderboard`: Get leaderboard data

- **Admin**
  - `GET /admin/users`: Get all users with progress
  - `GET /admin/user/{user_id}/progress`: Get detailed progress for a user

## Technologies Used

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- Lucide React (icons)
- Axios (API requests)

### Backend
- FastAPI
- Python
- SQLAlchemy (ORM)
- MySQL (database)
- Pydantic (data validation)
- JWT (authentication)

## Setup and Installation

### Prerequisites

- Node.js (v14 or later)
- Python (v3.8 or later)
- MySQL database

### Frontend

1. Navigate to the frontend directory:
   ```bash
   cd app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

### Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:
   ```bash
   python init_db.py
   python seed_main.py
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

## Usage

1. Open your browser and navigate to `http://localhost:3000` for the frontend.
2. Register a new account or log in with an existing one.
3. Browse available subjects and start taking quizzes.
4. Track your progress in the dashboard and compete on the leaderboard.

## Contributing

We welcome contributions from the community! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature-branch`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
