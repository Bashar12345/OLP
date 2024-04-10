import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
# username = os.getenv('DB_USERNAME')
# password = os.getenv('DB_PASSWORD')
# hostname = os.getenv('DB_HOSTNAME')
# port = os.getenv('DB_PORT')
# database_name = os.getenv('DB_NAME')

# # Construct the PostgreSQL connection URI
# postgres_uri = f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}?sslmode=require'

# Initialize Flask-SQLAlchemy
db = SQLAlchemy()

# Replace the placeholders with your actual credentials
username = 'citus'
password = 'mysql1234!-'
hostname = 'c-olp.6e3ox53w4dtrp6.postgres.cosmos.azure.com'
port = '5432'
database_name = 'citus'

COSMOSDB_CONN = os.getenv('COSMOSDB_CONN')

# Construct the PostgreSQL connection URI
postgres_uri = f'postgresql://{username}:{password}@{hostname}:{port}/{database_name}?sslmode=require'

# postgres_uri = 'postgres://citus:mysql1234!-@c-olp.6e3ox53w4dtrp6.postgres.cosmos.azure.com:5432/citus?sslmode=require'


# Configure the Flask application to use PostgreSQL
# app.config['SQLALCHEMY_DATABASE_URI'] = postgres_uri
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



# Define the Flask application configuration class
class Config:
    # Generate a secret key for the application
    SECRET_KEY = os.urandom(32)

    # Configure the Flask application to use PostgreSQL
    SQLALCHEMY_DATABASE_URI = postgres_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# ekhaner sob data r value environ e rakhte hobe
MYDIR = os.path.dirname(__file__)
