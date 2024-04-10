
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Replace the placeholders with your actual credentials
username = 'citus'
password = 'mysql1234!-'
hostname = 'c-olp.6e3ox53w4dtrp6.postgres.cosmos.azure.com'
port = '5432'
database_name = 'citus'


app = Flask(__name__)

# Construct the PostgreSQL connection URI
postgres_uri = f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}?sslmode=require'

# postgres_uri = 'postgres://citus:mysql1234!-@c-olp.6e3ox53w4dtrp6.postgres.cosmos.azure.com:5432/citus?sslmode=require'


# Configure the Flask application to use PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Try to create the database engine
try:
    engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")


# Define your models
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.String(255))
    instructor = db.Column(db.String(100))
    duration = db.Column(db.Integer)  # In minutes
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Course {self.title}>'

# Create the database tables (optional, if you have not created them yet)
with app.app_context():
    db.create_all()
    
# Create a route to test the database connection
@app.route('/test_db')
def test_db():
    # Query the database
    course = Course.query.first()

    # Check if a course was retrieved from the database
    if course:
        return f"Database connection successful! First course: {course.title}"
    else:
        return "Database connection failed or no data found."


# Routes and other application logic can go here

if __name__ == '__main__':
    app.run(debug=True)
