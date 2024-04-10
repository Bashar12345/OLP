import os
from flask import Flask
from flask_restx import Api
from .configaration import Config
from .models import db
from .courses.routes import courses
from .enrollments.routes import enrollments
from .for_errors.error_handler import errors

# Create an instance of Api for API documentation
api = Api(version='1.0', title='Online Learning Platform API',
          description='API endpoints for managing courses and enrollments')

def create_app(config_class=Config):
    app = Flask(__name__)

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
    app.register_blueprint(courses, url_prefix='/courses')
    app.register_blueprint(enrollments, url_prefix='/enrollments')
    app.register_blueprint(errors)

    # Integrate the API documentation setup with the Flask application
    from .courses.routes import courses_ns
    from .enrollments.routes import enrollments_ns
    api.add_namespace(courses_ns)
    api.add_namespace(enrollments_ns)
    api.init_app(app)

    return app
