"""This module contains the database connection and collections."""

from pymongo import MongoClient
import os

# MongoDB setup
client = MongoClient(os.getenv("MONGODB_URI"))
db = client["billmd"]
users_collection = db["users"]