from flask_pymongo import PyMongo
from pymongo import MongoClient

mongo = PyMongo()

def initialize_db(app):
    mongo.init_app(app)

client = MongoClient(app.confi["MONGO_URI"])
db = client["jackjay_data"]  
print(db.jackjay_data()) 
