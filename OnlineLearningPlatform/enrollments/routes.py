from flask import Blueprint, request
from flask_restx import Api, Namespace, Resource, fields

# Define Flask Blueprint and Namespace
enrollment_bp = Blueprint('enrollment_bp', __name__)
enrollment_ns = Namespace('enrollments', description='Enrollment operations')
api = Api(enrollment_bp)

# Define the data model for an enrollment
enrollment_model = enrollment_ns.model('Enrollment', {
    'student_name': fields.String(required=True, description='The name of the student'),
    'course_id': fields.Integer(required=True, description='The ID of the course to enroll in')
})

# Dummy data for testing
courses = [
    {'id': 1, 'title': 'Python Basics', 'description': 'Introduction to Python programming language', 'instructor': 'John Doe', 'duration': 60, 'price': 49.99},
    {'id': 2, 'title': 'Data Science Fundamentals', 'description': 'Introduction to data science concepts', 'instructor': 'Jane Smith', 'duration': 90, 'price': 79.99},
    {'id': 3, 'title': 'Web Development Crash Course', 'description': 'Learn the basics of web development', 'instructor': 'Sam Johnson', 'duration': 120, 'price': 99.99}
]

# Dummy data for testing
enrollments = [
    {'id': 1, 'student_name': 'Alice', 'course_id': 1},
    {'id': 2, 'student_name': 'Bob', 'course_id': 2},
    {'id': 3, 'student_name': 'Charlie', 'course_id': 1},
]


# Resource for enrolling students in a course and validating an enrollment
@enrollment_ns.route('/')
class EnrollmentService(Resource):
    @enrollment_ns.doc('enroll_student_and_validate')
    @enrollment_ns.expect(enrollment_model)
    def post(self):
        '''Enroll a student in a course or validate an enrollment'''
        enrollment_info = request.json
        student_name = enrollment_info.get('student_name')
        course_id = enrollment_info.get('course_id')

        # If the student_name and course_id are provided, validate enrollment
        if student_name and course_id:
            existing_enrollment = next((enrollment for enrollment in enrollments if enrollment['student_name'] == student_name and enrollment['course_id'] == course_id), None)
            if existing_enrollment:
                return {'message': 'Enrollment is valid'}, 200
            else:
                return {'message': 'Enrollment is not valid'}, 404

        # Otherwise, enroll the student in the course
        else:
            # Validate if the course_id exists (dummy validation)
            if course_id not in [course['id'] for course in courses]:
                return {'message': 'Invalid course ID'}, 400

            new_enrollment = {'student_name': student_name, 'course_id': course_id}
            enrollments.append(new_enrollment)
            return new_enrollment, 201


# Description of the Enrollment API
enrollment_api_description = """
Enrollment API
- POST /enrollments: Allow students to enroll in a course or validate an enrollment.
"""

# Assign the Blueprint to the Flask app
# app.register_blueprint(enrollment_bp)
