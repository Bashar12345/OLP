from flask import Blueprint, request, jsonify
from OnlineLearningPlatform.models import Enrollment, db

# Create a blueprint for the enrollments routes
enrollments = Blueprint('enrollments', __name__)

# Route to allow students to enroll in a course
@enrollments.route('/enrollments', methods=['POST'])
def enroll_student():
    data = request.json
    student_name = data.get('student_name')
    course_id = data.get('course_id')

    # Check if the student is already enrolled in the course
    existing_enrollment = Enrollment.query.filter_by(student_name=student_name, course_id=course_id).first()
    if existing_enrollment:
        return jsonify({'message': 'Student is already enrolled in this course'}), 400

    # Create a new enrollment
    new_enrollment = Enrollment(student_name=student_name, course_id=course_id)
    db.session.add(new_enrollment)
    db.session.commit()

    return jsonify({'message': 'Enrollment successful'}), 201
