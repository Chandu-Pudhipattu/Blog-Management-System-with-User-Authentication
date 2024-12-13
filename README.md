# Digital Dairy project
 Raise your voice to Inspire the Nation....

## About 
This web application built with Django that allows users to create, edit, and delete blog posts, as well as manage user accounts. This project demonstrates the core functionalities of a blog platform and includes user authentication, and a responsive design.

## Features
- User authentication (login, logout, and registration)
- Create, read, update, and delete (CRUD) functionality for blog posts
- Responsive design for mobile and desktop
- Pagination for blog post lists
- Admin panel for managing users and posts

## Technologies Used
- **Backend:** Django, Python
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (for local development)

## Setup and Installation

### Prerequisites
- Python (3.9 or higher)
- pip (Python package manager)
- Virtualenv (optional but recommended)
- Git
- django

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows, use myenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate


4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser:
   Go to `http://127.0.0.1:8000/`

## Usage
- **Homepage:** Displays a list of blog posts with pagination.
- **Admin Panel:** Manage posts and users at `/admin/`.
- **User Features:**
  - Register, login, and logout
  - Create, edit, and delete posts
