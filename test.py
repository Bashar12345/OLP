import unittest
import json
from server import app

class TestCourseEnrollmentAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_create_course(self):
        # Define a sample course data
        sample_course_data = {
            "title": "Introduction to Python Programming",
            "instructor": "John Doe",
            "price": 49.99,
            "duration": 30
        }

        # Make a POST request to create a new course
        response = self.app.post('/courses', json=sample_course_data)

        # Assert that the status code is 201 (created)
        self.assertEqual(response.status_code, 201)

        # Convert the response data from JSON to a Python dictionary
        response_data = json.loads(response.data)

        # Assert that the returned course data matches the sample course data
        self.assertEqual(response_data['title'], sample_course_data['title'])
        self.assertEqual(response_data['instructor'], sample_course_data['instructor'])
        self.assertEqual(response_data['price'], sample_course_data['price'])
        self.assertEqual(response_data['duration'], sample_course_data['duration'])

    def test_enroll_student(self):
        # Define a sample enrollment data
        sample_enrollment_data = {
            "student_name": "Alice",
            "course_id": 1
        }

        # Make a POST request to enroll a student in a course
        response = self.app.post('/enrollments', json=sample_enrollment_data)

        # Assert that the status code is 201 (created)
        self.assertEqual(response.status_code, 201)

        # Convert the response data from JSON to a Python dictionary
        response_data = json.loads(response.data)

        # Assert that the returned enrollment data matches the sample enrollment data
        self.assertEqual(response_data['student_name'], sample_enrollment_data['student_name'])
        self.assertEqual(response_data['course_id'], sample_enrollment_data['course_id'])

    def test_validate_enrollment(self):
        # Define an invalid enrollment data (non-existent course ID)
        invalid_enrollment_data = {
            "student_name": "Bob",
            "course_id": 999  # Assuming this course ID does not exist
        }

        # Make a POST request to validate the enrollment
        response = self.app.post('/enrollments', json=invalid_enrollment_data)

        # Assert that the status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Assert that the returned message indicates an invalid course ID
        self.assertIn('Invalid course ID', response.data.decode())

if __name__ == '__main__':
    unittest.main()
