from flask import Blueprint, request, abort
from flask_restx import Api, Namespace, Resource, fields


# Define Flask Blueprint and Namespace
enrollment_bp = Blueprint('enrollment_bp', __name__)
enrollment_ns = Namespace('enrollments', description='Enrollment operations')
api = Api(enrollment_bp)

# Define the data model for an enrollment
enrollment_model = enrollment_ns.model('Enrollment', {
    'id': fields.Integer(readonly=True, description='The enrollment unique identifier'),
    'student_name': fields.String(required=True, description='The name of the student'),
    'course_id': fields.Integer(required=True, description='The ID of the course to enroll in')
})

# Dummy data for testing
enrollments = [
    {'id': 1, 'student_name': 'Alice', 'course_id': 1},
    {'id': 2, 'student_name': 'Bob', 'course_id': 2},
    {'id': 3, 'student_name': 'Charlie', 'course_id': 1},
]


# Resource for enrolling students in a course
@enrollment_ns.route('/')
class EnrollmentList(Resource):
    @enrollment_ns.doc('enroll_student')
    @enrollment_ns.expect(enrollment_model)
    def post(self):
        '''Enroll a student in a course'''
        new_enrollment = request.json
        # Validate if the course_id exists (dummy validation)
        course_id = new_enrollment.get('course_id')
        if course_id not in [course['id'] for course in courses]:
            return {'message': 'Invalid course ID'}, 400

        new_enrollment['id'] = len(enrollments) + 1
        enrollments.append(new_enrollment)
        return new_enrollment, 201

    @enrollment_ns.doc('validate_enrollment')
    def get(self):
        '''Check if an enrollment is valid'''
        student_name = request.args.get('student_name')
        course_id = request.args.get('course_id')

        # Check if the provided student name and course ID match an existing enrollment
        existing_enrollment = next((enrollment for enrollment in enrollments if enrollment['student_name'] == student_name and enrollment['course_id'] == int(course_id)), None)
        if existing_enrollment:
            return {'message': 'Enrollment is valid'}, 200
        else:
            return {'message': 'Enrollment is not valid'}, 404


# Description of the Enrollment API
enrollment_api_description = """
Enrollment API
- POST /enrollments: Allow students to enroll in a course.
"""

# Assign the Blueprint to the Flask app
# app.register_blueprint(enrollment_bp)
