from flask import Blueprint, request, jsonify
from OnlineLearningPlatform.models import Course, db
from . import course_model

# Create a blueprint for the courses routes
courses = Blueprint('courses', __name__)

# Route to retrieve a list of available courses
@courses.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    return jsonify([course_model.dump(course) for course in courses])

# Route to retrieve a specific course by its ID
@courses.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get_or_404(course_id)
    return course_model.dump(course)

# Route to create a new course
@courses.route('/courses', methods=['POST'])
def create_course():
    data = request.json
    new_course = Course(
        title=data.get('title'),
        description=data.get('description'),
        instructor=data.get('instructor'),
        duration=data.get('duration'),
        price=data.get('price')
    )
    db.session.add(new_course)
    db.session.commit()
    return course_model.dump(new_course), 201
