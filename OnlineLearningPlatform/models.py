# models.py
from OnlineLearningPlatform import db

# Define the Course model
class Course(db.Model):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    instructor = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the Enrollment model
class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.Date, nullable=False)

