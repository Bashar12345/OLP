#server.py
import os
from OnlineLearningPlatform import app

port = int(os.environ.get("PORT", 5000)) 

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
