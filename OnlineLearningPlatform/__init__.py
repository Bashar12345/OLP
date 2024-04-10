# __init__.py

from flask import Flask
from flask_restx import Api
from .configaration import Config 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)  

# Initialize Flask-SQLAlchemy
db=SQLAlchemy(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Create an application context
with app.app_context():
    # Create the tables
    db.create_all()


api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')


# db.init_app(app)  # Initialize the db with the Flask app
# Try to create the database engine
# Import and register blueprints/namespaces
from OnlineLearningPlatform.courses.routes import course_ns  # noqa: E402
from OnlineLearningPlatform.enrollments.routes import enrollment_ns  # noqa: E402


api.add_namespace(course_ns)
api.add_namespace(enrollment_ns)












# from flask import Flask
# from OnlineLearningPlatform.courses.routes import course_ns
# from OnlineLearningPlatform.enrollments.routes import enrollment_ns
# # from OnlineLearningPlatform.for_errors.error_handler import error_handler
# from flask_restx import Api

# app = Flask(__name__)

# api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')



# # Register namespaces
# api.add_namespace(course_ns)
# api.add_namespace(enrollment_ns)







































# # from flask import Flask
# # from OnlineLearningPlatform.courses.routes import course_ns
# # from OnlineLearningPlatform.enrollments.routes import enrollment_ns
# # # from OnlineLearningPlatform.for_errors.error_handler import error_handler
# # from flask_restx import Api

# # app = Flask(__name__)
# # api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')

# # # Register namespaces
# # api.add_namespace(course_ns)
# # api.add_namespace(enrollment_ns)

# # # Register error handler
# # # app.register_blueprint(error_handler)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# # import os
# # from flask import Flask
# # from flask_restx import Api
# # from .configaration import Config
# # from .models import db
# # from .courses.routes import courses
# # from .enrollments.routes import enrollments
# # from .for_errors.error_handler import errors

# # # Create an instance of Api for API documentation
# # api = Api(version='1.0', title='Online Learning Platform API',
# #           description='API endpoints for managing courses and enrollments')

# # def create_app(config_class=Config):
# #     app = Flask(__name__)

# #     # Load configurations from Config class
# #     app.config.from_object(config_class)

# #     # Initialize SQLAlchemy with the app context
# #     db.init_app(app)

# #     # Try to create the database engine
# #     with app.app_context():
# #         try:
# #             engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
# #             # Check if the connection is successful
# #             connection = engine.connect()
# #             connection.close()
# #             print("Database connection successful!")
# #         except Exception as e:
# #             print(f"Database connection failed: {e}")

# #     # Register blueprints
# #     app.register_blueprint(courses, url_prefix='/courses')
# #     app.register_blueprint(enrollments, url_prefix='/enrollments')
# #     app.register_blueprint(errors)

# #     # Integrate the API documentation setup with the Flask application
# #     from .courses.routes import courses_ns
# #     from .enrollments.routes import enrollments_ns
# #     api.add_namespace(courses_ns)
# #     api.add_namespace(enrollments_ns)
# #     api.init_app(app)

# #     return app


# from flask import Flask
# from flask_restx import Api, Resource, fields

# app = Flask(__name__)
# api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')

# course_model = api.model('Course', {
#     'id': fields.Integer(readonly=True, description='The course unique identifier'),
#     'title': fields.String(required=True, description='The course title'),
#     'description': fields.String(required=True, description='The course description'),
#     'instructor': fields.String(required=True, description='The course instructor'),
#     'duration': fields.Integer(required=True, description='The duration of the course in minutes'),
#     'price': fields.Float(required=True, description='The price of the course')
# })

# enrollment_model = api.model('Enrollment', {
#     'id': fields.Integer(readonly=True, description='The enrollment unique identifier'),
#     'student_name': fields.String(required=True, description='The name of the student'),
#     'course_id': fields.Integer(required=True, description='The ID of the course to enroll in')
# })

# # Dummy data for testing
# courses = [
#     {'id': 1, 'title': 'Python Basics', 'description': 'Introduction to Python programming language', 'instructor': 'John Doe', 'duration': 60, 'price': 49.99},
#     {'id': 2, 'title': 'Data Science Fundamentals', 'description': 'Introduction to data science concepts', 'instructor': 'Jane Smith', 'duration': 90, 'price': 79.99},
#     {'id': 3, 'title': 'Web Development Crash Course', 'description': 'Learn the basics of web development', 'instructor': 'Sam Johnson', 'duration': 120, 'price': 99.99}
# ]

# enrollments = [
#     {'id': 1, 'student_name': 'Alice', 'course_id': 1},
#     {'id': 2, 'student_name': 'Bob', 'course_id': 2},
#     {'id': 3, 'student_name': 'Charlie', 'course_id': 1},
# ]

# @api.route('/courses')
# class CourseList(Resource):
#     @api.doc('list_courses')
#     def get(self):
#         '''List all courses'''
#         return [course for course in courses]

#     @api.doc('create_course')
#     @api.expect(course_model)
#     def post(self):
#         '''Create a new course'''
#         new_course = api.payload
#         new_course['id'] = len(courses) + 1
#         courses.append(new_course)
#         return new_course, 201

# @api.route('/courses/<int:id>')
# @api.response(404, 'Course not found')
# class Course(Resource):
#     @api.doc('get_course')
#     def get(self, id):
#         '''Fetch a course by its ID'''
#         for course in courses:
#             if course['id'] == id:
#                 return course
#         api.abort(404, "Course {} doesn't exist".format(id))

# @api.route('/enrollments')
# class EnrollmentList(Resource):
#     @api.doc('enroll_student')
#     @api.expect(enrollment_model)
#     def post(self):
#         '''Enroll a student in a course'''
#         new_enrollment = api.payload
#         new_enrollment['id'] = len(enrollments) + 1
#         enrollments.append(new_enrollment)
#         return new_enrollment, 201

# if __name__ == '__main__':
#     app.run(debug=True)
