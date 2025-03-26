# University Management System (Django)

A Django-based **University Management System** that allows students and administrators to manage academic operations efficiently. This project includes role-based access, course management, student records, and notifications.

## Features
- **Authentication & Authorization**
  - Custom login & registration system
  - Role-based access control for students and admins
- **Student Management**
  - View & manage student profiles
  - Enroll in courses
- **Admin Dashboard**
  - Manage departments, courses, and students
  - Assign roles and permissions
- **Notifications System**
  - Automatic email notifications using **Celery** and **Django signals**
- **Security & Middleware**
  - Custom middleware for access control
  - Secure password generation for new users

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)
- **Background Tasks:** Celery
- **Authentication:** Django built-in authentication

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AbirHasanSupta/UniversityManagement_Django.git
   cd UniversityManagement_Django
   ```
2. **Create a virtual environment & activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   *Follow the prompt to set up an admin account.*
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   The app will be available at **http://127.0.0.1:8000/**

## Usage
- **Admin Panel:** `http://127.0.0.1:8000/admin/`
- **Student Dashboard:** Accessible after login
- **Course Management:** Admins can add/update/delete courses
- **Notifications:** Automatic email notifications for new users

## Future Enhancements
- API support using Django Rest Framework (DRF)
- Integration with payment gateways for course fees
- Improved UI using React/Vue
- Docker support for easy deployment

