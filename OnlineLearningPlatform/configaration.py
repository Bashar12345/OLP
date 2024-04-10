# configuration.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')
hostname = os.getenv('DB_HOSTNAME')
port = os.getenv('DB_PORT')  # Ensure this value is properly set in your .env file
database_name = os.getenv('DB_NAME')

# Construct the PostgreSQL connection URI
# Handle the case where port might be None
if port:
    postgres_uri = f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}?sslmode=require'
else:
    postgres_uri = f'postgresql://{username}:{password}@{hostname}/{database_name}?sslmode=require'

try:
    # Create the SQLAlchemy engine
    engine = create_engine(postgres_uri)
    connection = engine.connect()
    connection.close()

    print("Database connection successful!")
except Exception as e:
    print(f"Database connection failed: {e}")

# Define the Flask application configuration class
class Config:
    # Generate a secret key for the application
    SECRET_KEY = os.urandom(32)

    # Configure the Flask application to use PostgreSQL
    SQLALCHEMY_DATABASE_URI = postgres_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
