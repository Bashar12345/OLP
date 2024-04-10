from flask import Blueprint, request
from flask_restx import Api, Namespace, Resource, fields
from .utils import CourseService



# Define Flask Blueprint and Namespace
course_bp = Blueprint("course_bp", __name__)
course_ns = Namespace("courses", description="Course operations")
api = Api(course_bp)

# Define the data model for a course
course_model = course_ns.model(
    "Course",
    {
        "id": fields.Integer(readonly=True, description="The course unique identifier"),
        "title": fields.String(required=True, description="The course title"),
        "description": fields.String(
            required=True, description="The course description"
        ),
        "instructor": fields.String(required=True, description="The course instructor"),
        "duration": fields.Integer(
            required=True, description="The duration of the course in minutes"
        ),
        "price": fields.Float(required=True, description="The price of the course"),
    },
)


# Resource for listing and creating courses
@course_ns.route("/")
class CourseList(Resource):
    @course_ns.doc("list_courses")
    def get(self):
        """List all courses"""
        courses = CourseService.get_courses()
        return courses

    @course_ns.doc("create_course")
    @course_ns.expect(course_model)
    def post(self):
        """Create a new course"""
        data = request.json
        new_course = CourseService.create_course(data['title'], data['description'], data['instructor'], data['duration'], data['price'])
        # Convert new_course to JSON or any desired format
        return new_course


# Resource for retrieving, updating, and deleting a specific course
@course_ns.route("/<int:id>")
@course_ns.param("id", "The course identifier")
@course_ns.response(404, "Course not found")
class CourseItem(Resource):
    @course_ns.doc("get_course")
    @course_ns.marshal_with(course_model)
    def get(self, id):
        """Retrieve a course"""
        course = CourseService.get_course_by_id(id)
        return course




# Resource for filtering courses based on parameters
@course_ns.route("/filter")
class CourseFilter(Resource):
    @course_ns.doc("filter_courses")
    @course_ns.param("instructor", "Filter by instructor")
    @course_ns.param("price", "Filter by price")
    @course_ns.param("duration", "Filter by duration")
    def get(self):
        """Filter courses by various properties"""
        instructor = request.args.get("instructor")
        price = request.args.get("price")
        duration = request.args.get("duration")
        courses = CourseService.filter_courses(instructor, price, duration)
        return courses


# Description of the Course API
course_api_description = """
Course API
- GET /courses: Retrieve a list of available courses.
- GET /courses/:id: Retrieve a specific course by its ID.
- POST /courses: Create a new course
"""

# Assign the Blueprint to the Flask app
# app.register_blueprint(course_bp)






    # @course_ns.doc("update_course")
    # @course_ns.expect(course_model)
    # @course_ns.marshal_with(course_model)
    # def put(self, id):
    #     """Update a course"""
    #     course = CourseModel.query.get(id)
    #     if not course:
    #         course_ns.abort(404, f"Course {id} not found")
    #     data = request.json
    #     course.update(data)
    #     db.session.commit()
    #     return data

    # @course_ns.doc("delete_course")
    # @course_ns.response(204, "Course deleted")
    # def delete(self, id):
    #     """Delete a course"""
    #     course = CourseModel.query.get(id)
    #     if not course:
    #         course_ns.abort(404, f"Course {id} not found")
    #     db.session.delete(course)
    #     db.session.commit()
    #     return "", 204















# # Define the data model for a course
# course_model = course_ns.model('Course', {
#     'id': fields.Integer(readonly=True, description='The course unique identifier'),
#     'title': fields.String(required=True, description='The course title'),
#     'description': fields.String(required=True, description='The course description'),
#     'instructor': fields.String(required=True, description='The course instructor'),
#     'duration': fields.Integer(required=True, description='The duration of the course in minutes'),
#     'price': fields.Float(required=True, description='The price of the course')
# })

# # Dummy data for testing
# courses = [
#     {'id': 1, 'title': 'Python Basics', 'description': 'Introduction to Python programming language', 'instructor': 'John Doe', 'duration': 60, 'price': 49.99},
#     {'id': 2, 'title': 'Data Science Fundamentals', 'description': 'Introduction to data science concepts', 'instructor': 'Jane Smith', 'duration': 90, 'price': 79.99},
#     {'id': 3, 'title': 'Web Development Crash Course', 'description': 'Learn the basics of web development', 'instructor': 'Sam Johnson', 'duration': 120, 'price': 99.99}
# ]
