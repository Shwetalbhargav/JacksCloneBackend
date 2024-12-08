from flask import Blueprint, jsonify
from app.scraper import scrape_jackjay
from app.database import mongo
from datetime import datetime
from app.config import APP_START_TIME  

scraper_routes = Blueprint("scraper_routes", __name__)

@scraper_routes.route("/test_db", methods=["GET"])
def test_db():
    try:
        db_status = mongo.cx.admin.command("ping")
        return jsonify({"status": "connected", "db_status": db_status}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@scraper_routes.route("/scrape", methods=["GET"])
def scrape_and_store():
    try:
        # Scrape data
        #scraped_data = scrape_jackjay()
        print("Using mock data for testing...")
        scraped_data = [
            {"title": "Test Title 1", "description": "Test Description 1"},
            {"title": "Test Title 2", "description": "Test Description 2"}
        ]

        # Store data in MongoDB
        db = mongo.db.jackjay_data
        db.insert_many(scraped_data)

        return jsonify({"message": "Data scraped and stored successfully!", "data": scraped_data}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@scraper_routes.route("/view_data", methods=["GET"])
def view_data():
    try:
        db = mongo.db.jackjay_data
        # Retrieve all documents from the collection
        data = list(db.find({}))
        
        # Ensure the data is serializable (MongoDB ObjectId can cause issues)
        for doc in data:
            doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
        
        return jsonify(data), 200
    except Exception as e:
        # Handle any unexpected errors and return an error message
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@scraper_routes.route("/status", methods=["GET"])
def check_status():
    try:
        # Database connection status
        db_status = mongo.cx.admin.command("ping")
        db_connected = True if db_status.get("ok") == 1 else False

        # Number of records in the collection
        collection = mongo.db.jackjay_data
        record_count = collection.count_documents({})

        # Uptime
        uptime_duration = datetime.now() - APP_START_TIME
        uptime_seconds = int(uptime_duration.total_seconds())
        uptime_human_readable = str(uptime_duration).split('.')[0]

        return jsonify({
            "status": "running",
            "database": {
                "connected": db_connected,
                "record_count": record_count
            },
            "uptime": {
                "seconds": uptime_seconds,
                "human_readable": uptime_human_readable
            }
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


@scraper_routes.route("/", methods=["GET"])
def home():
    try:
        
        return jsonify({"message": "Welcome to the Flask API!"}), 200
    except Exception as e:
     
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

