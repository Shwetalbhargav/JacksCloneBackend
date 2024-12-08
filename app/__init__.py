from flask import Flask
from app.database import initialize_db
from app.routes import scraper_routes




def create_app():
    app = Flask(__name__)

    # MongoDB configuration
    app.config["MONGO_URI"] = "mongodb+srv://shwetal:12345@cluster0.kvpwk.mongodb.net/jackjay?retryWrites=true&w=majority"

    # Initialize the database
    initialize_db(app)





    # Register routes
    from app.routes import scraper_routes
    app.register_blueprint(scraper_routes)

    return app
