from flask import Flask
import mysql.connector

def create_app():
    app = Flask(__name__)
    app.secret_key = "your_secret_key"

    # DB Configuration
    app.config['DB'] = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Reset@123",
        database="Student_db"
    )

    from .routes import register_routes
    register_routes(app)

    return app
