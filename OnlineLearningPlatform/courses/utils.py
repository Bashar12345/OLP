from OnlineLearningPlatform.models import db, Course as CourseModel


class CourseService:
    @staticmethod
    def get_courses():
        return CourseModel.query.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        new_course = CourseModel(
            title=title,
            description=description,
            instructor=instructor,
            duration=duration,
            price=price,
        )
        db.session.add(new_course)
        db.session.commit()
        return new_course

    @staticmethod
    def get_course_by_id(course_id):
        return CourseModel.query.get(course_id)

    @staticmethod
    def filter_courses(instructor=None, price=None, duration=None):
        query = CourseModel.query
        if instructor:
            query = query.filter_by(instructor=instructor)
        if price:
            query = query.filter(CourseModel.price <= price)
        if duration:
            query = query.filter(CourseModel.duration <= duration)
        return query.all()
