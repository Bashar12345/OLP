from OnlineLearningPlatform.models import db, Course, Enrollment as EnrollmentModel


class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id):
        new_enrollment = EnrollmentModel(student_name=student_name, course_id=course_id)
        db.session.add(new_enrollment)
        db.session.commit()
        return new_enrollment

    @staticmethod
    def validate_enrollment(course_id):
        course = Course.query.get(course_id)
        return course is not None
