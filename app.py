"""This is the main file of the application. It contains the Flask app and all routes."""

from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)

from flask import Flask
from services.user.routes import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

