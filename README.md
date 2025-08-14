# CodeTech - Interactive Learning Platform

A modern, interactive learning platform built with Next.js, FastAPI, and SQLite. Features quiz-based learning and progress tracking.

## 🚀 Features

### For Students
- **Interactive Quizzes**: Take quizzes on various programming subjects
- **Progress Tracking**: Monitor your learning progress across subjects
- **Leaderboard**: Compete with other students
- **Personal Dashboard**: View your stats, recent activity, and achievements
- **Subject-based Learning**: Structured learning paths for different programming languages

<!-- Admin features removed in MVP -->

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Shadcn/ui** - Modern UI components
- **Lucide React** - Beautiful icons

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight database
- **JWT** - JSON Web Token authentication
- **Passlib** - Password hashing
- **Pydantic** - Data validation

## 📦 Installation

### Prerequisites
- Node.js 18+ 
- Python 3.8+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the backend server**:
   ```bash
   python main.py
   ```
   The server will run on `http://localhost:8000`

### Frontend Setup

1. **Install Node.js dependencies**:
   ```bash
   npm install
   ```

2. **Start the development server**:
   ```bash
   npm run dev
   ```
   The frontend will run on `http://localhost:3000`

## 🔐 Authentication

### Demo Accounts

Use your own account to sign in. Admin role is not part of the MVP.

### User Roles

- **Student**: Can take quizzes, view progress, access learning materials

## 📚 Available Subjects

1. **Python Programming** - 5 levels, 50 quizzes
   - Variables & Data Types
   - Control Structures
   - Functions & Modules
   - Object-Oriented Programming
   - Advanced Topics

2. **Machine Learning** - 4 levels, 40 quizzes
   - ML Fundamentals
   - Supervised Learning
   - Unsupervised Learning
   - Deep Learning Basics

3. **JavaScript** - 6 levels, 30 quizzes
   - JavaScript Basics
   - Control Flow
   - Functions & ES6
   - DOM & Events
   - Arrays & Objects
   - Advanced JavaScript

4. **C Programming** - 6 levels, 30 quizzes
   - C Basics
   - Control Flow
   - Functions
   - Pointers & Arrays
   - Strings & Structures
   - File I/O & Advanced

## 🎯 How to Use

### For Students

1. **Sign Up/Login**: Use the demo credentials or create a new account
2. **Browse Subjects**: Explore available learning paths
3. **Take Quizzes**: Start with level 1 and progress through levels
4. **Track Progress**: Monitor your completion rate and scores
5. **View Leaderboard**: See how you rank against other students

<!-- Admin workflow removed in MVP -->

## 🔧 API Endpoints

### Authentication
- `POST /signup` - Register new user
- `POST /login` - User login
- `GET /me` - Get current user info

### Quizzes
- `GET /quiz/{subject_id}/{level_id}` - Get quiz questions
- `POST /quiz/{subject_id}/{level_id}/submit` - Submit quiz answers

### User Progress
- `GET /user/subjects` - Get user's subject progress
- `GET /user/activity` - Get user's recent activity
- `GET /user/stats` - Get user statistics

<!-- Admin endpoints removed in MVP -->

### Public
- `GET /subjects` - Get all subjects
- `GET /leaderboard` - Get leaderboard data
- `GET /dashboard-data` - Get dashboard statistics

## 🧪 Testing

Run the API test script to verify all endpoints are working:

```bash
cd backend
python test_api.py
```

## 📁 Project Structure

```
CodeTech/
├── app/                    # Next.js frontend pages
<!-- Admin dashboard removed in MVP -->
│   ├── dashboard/         # User dashboard
│   ├── login/            # Login page
│   ├── quiz/             # Quiz pages
│   └── subject/          # Subject pages
├── backend/               # FastAPI backend
│   ├── main.py           # Main API server
<!-- Admin user creation script not used in MVP -->
│   └── test_api.py       # API testing script
├── components/            # React components
│   └── ui/               # Shadcn/ui components
├── lib/                   # Utility functions
│   └── api.ts            # API client functions
└── public/               # Static assets
```

## 🚀 Deployment

### Backend Deployment
1. Install dependencies: `pip install -r requirements.txt`
2. Set environment variables for production
3. Use a production WSGI server like Gunicorn
4. Deploy to your preferred hosting service

### Frontend Deployment
1. Build the project: `npm run build`
2. Deploy the `out` directory to your hosting service
3. Configure environment variables for production API URL

## 🔒 Security Features

- **JWT Authentication**: Secure token-based authentication
- **Password Hashing**: Bcrypt password hashing
<!-- Admin role-based access removed in MVP -->
- **CORS Protection**: Configured for development and production
- **Input Validation**: Pydantic models for data validation

## 🎨 UI/UX Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface
- **Progress Visualization**: Charts and progress bars
- **Interactive Elements**: Hover effects and animations
- **Accessibility**: ARIA labels and keyboard navigation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

If you encounter any issues:

1. Check the console for error messages
2. Verify the backend server is running
3. Ensure all dependencies are installed
4. Check the API test script for endpoint verification

## 🎉 Getting Started

1. Clone the repository
2. Follow the installation steps above
3. Start both backend and frontend servers
4. Login with demo credentials
5. Start learning!

---

**Happy Learning! 🚀** 