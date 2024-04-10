#server.py
import os
from flask import Flask
from OnlineLearningPlatform.courses.routes import course_ns
from OnlineLearningPlatform.enrollments.routes import enrollment_ns
# from OnlineLearningPlatform.for_errors.error_handler import error_handler
from flask_restx import Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Online Learning Platform API', description='An API for managing courses and enrollments')

# Register namespaces
api.add_namespace(course_ns)
api.add_namespace(enrollment_ns)

# Register error handler
# app.register_blueprint(error_handler)

port = int(os.environ.get("PORT", 5050)) 

if __name__ == '__main__':
   
   app.run(debug=True, port=port, host='0.0.0.0')
   print("server started")

    # app.run(debug=True, host='0.0.0.0:5000')

# if __name__ == '__main__':
#     HOST = environ.get('SERVER_HOST', 'localhost')
#     try:
#         PORT = int(environ.get('SERVER_PORT', '5555'))
#     except ValueError:
#         PORT = 5555
#     app.run(HOST, PORT,debug=True)
#     print("server started")
