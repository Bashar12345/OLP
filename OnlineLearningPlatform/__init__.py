import os
from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from .configaration import Config
from .models import db
from flask_restx import Api, fields

Project_DIR = os.path.dirname(__file__)
print(Project_DIR)

# Create an instance of Api for API documentation
api = Api(version='1.0', title='Online Learning Platform API',
        description='API endpoints for managing courses and enrollments')

# Define models for serialization
course_model = api.model('Course', {
    'course_id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'instructor': fields.String,
    'duration': fields.Integer,
    'price': fields.Float
})

enrollment_model = api.model('Enrollment', {
    'enrollment_id': fields.Integer,
    'student_name': fields.String,
    'course_id': fields.Integer,
    'enrollment_date': fields.String
})

# Define API namespaces
courses_ns = api.namespace('courses', description='Operations related to courses')
enrollments_ns = api.namespace('enrollments', description='Operations related to enrollments')


def create_app(config_class=Config):
    app = Flask(__name__)  # run all package as initial flask app

    # Load configurations from Config class
    app.config.from_object(config_class)

    # Initialize SQLAlchemy with the app context
    db.init_app(app)

    # Try to create the database engine
    with app.app_context():
        try:
            engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
            # Check if the connection is successful
            connection = engine.connect()
            connection.close()
            print("Database connection successful!")
        except Exception as e:
            print(f"Database connection failed: {e}")

    # Register blueprints
    from OnlineLearningPlatform.courses.routes import courses
    from OnlineLearningPlatform.enrollments.routes import enrollments
    from OnlineLearningPlatform.for_errors.error_handler import errors

    app.register_blueprint(courses)
    app.register_blueprint(enrollments)
    app.register_blueprint(errors)


    # Integrate the API documentation setup with the Flask application
    api.init_app(app)

    return app


