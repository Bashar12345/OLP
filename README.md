---

# Online Learning Platform

The Online Learning Platform is a Flask-based web application that provides API endpoints for managing courses and enrollments.

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository_url>
```

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of the project and define the necessary environment variables:

```bash
COSMOSDB_CONN=<your_cosmosdb_connection_string>
SQLALCHEMY_DATABASE_URI=<your_database_uri>
```

### 4. Run the Application

Run the Flask application:

```bash
python server.py
```

## API Endpoints

### Courses

- **GET /courses**: Retrieve a list of available courses.
- **GET /courses/:id**: Retrieve a specific course by its ID.
- **POST /courses**: Create a new course.

Example usage:

```bash
# Retrieve all courses
curl http://localhost:5000/courses

# Retrieve a specific course by ID
curl http://localhost:5000/courses/1

# Create a new course
curl -X POST -H "Content-Type: application/json" -d '{"title": "New Course", "description": "Description of the new course", "instructor": "John Doe", "duration": 60, "price": 49.99}' http://localhost:5000/courses
```

### Enrollments

- **POST /enrollments**: Allow students to enroll in a course.

Example usage:

```bash
# Enroll a student in a course
curl -X POST -H "Content-Type: application/json" -d '{"student_name": "Alice", "course_id": 1, "enrollment_date": "2024-04-12"}' http://localhost:5000/enrollments
```

## Dependencies

- Flask: Web framework for building the application.
- Flask-RESTx: Extension for building REST APIs with Flask.
- Flask-SQLAlchemy: Flask extension for working with SQLAlchemy, providing ORM capabilities.
- python-dotenv: Python module for parsing `.env` files to manage environment variables.

---
