from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = PyMongo()

def initialize_db(app):
    # Initialize PyMongo with Flask app
    mongo.init_app(app)

    # Use MongoClient for manual operations (inside the function scope)
    client = MongoClient(app.config["MONGO_URI"])
    db = client["jackjay"]  # Replace "jackjay" with your actual database name
    print(f"Connected to MongoDB database: {db.name}")
