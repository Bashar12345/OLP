from flask import Flask
from flask_restx import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')

course_model = api.model('Course', {
    'id': fields.Integer(readonly=True, description='The course unique identifier'),
    'title': fields.String(required=True, description='The course title'),
    'description': fields.String(required=True, description='The course description'),
    'instructor': fields.String(required=True, description='The course instructor'),
    'duration': fields.Integer(required=True, description='The duration of the course in minutes'),
    'price': fields.Float(required=True, description='The price of the course')
})

enrollment_model = api.model('Enrollment', {
    'id': fields.Integer(readonly=True, description='The enrollment unique identifier'),
    'student_name': fields.String(required=True, description='The name of the student'),
    'course_id': fields.Integer(required=True, description='The ID of the course to enroll in')
})

# Dummy data for testing
courses = [
    {'id': 1, 'title': 'Python Basics', 'description': 'Introduction to Python programming language', 'instructor': 'John Doe', 'duration': 60, 'price': 49.99},
    {'id': 2, 'title': 'Data Science Fundamentals', 'description': 'Introduction to data science concepts', 'instructor': 'Jane Smith', 'duration': 90, 'price': 79.99},
    {'id': 3, 'title': 'Web Development Crash Course', 'description': 'Learn the basics of web development', 'instructor': 'Sam Johnson', 'duration': 120, 'price': 99.99}
]

enrollments = [
    {'id': 1, 'student_name': 'Alice', 'course_id': 1},
    {'id': 2, 'student_name': 'Bob', 'course_id': 2},
    {'id': 3, 'student_name': 'Charlie', 'course_id': 1},
]

@api.route('/courses')
class CourseList(Resource):
    @api.doc('list_courses')
    def get(self):
        '''List all courses'''
        return [course for course in courses]

    @api.doc('create_course')
    @api.expect(course_model)
    def post(self):
        '''Create a new course'''
        new_course = api.payload
        new_course['id'] = len(courses) + 1
        courses.append(new_course)
        return new_course, 201

@api.route('/courses/<int:id>')
@api.response(404, 'Course not found')
class Course(Resource):
    @api.doc('get_course')
    def get(self, id):
        '''Fetch a course by its ID'''
        for course in courses:
            if course['id'] == id:
                return course
        api.abort(404, "Course {} doesn't exist".format(id))

@api.route('/enrollments')
class EnrollmentList(Resource):
    @api.doc('enroll_student')
    @api.expect(enrollment_model)
    def post(self):
        '''Enroll a student in a course'''
        new_enrollment = api.payload
        new_enrollment['id'] = len(enrollments) + 1
        enrollments.append(new_enrollment)
        return new_enrollment, 201

if __name__ == '__main__':
    app.run(debug=True)
