import bcrypt
from bson import ObjectId
from services.user import models
import db


def update_user(user: models.UserUpdateRequest):
    """Update the user in the database.
    
    Args:
        user: models.UserUpdateRequest - The user to update.
    """
    # Hash the password
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    
    db.users_collection.update_one(
        {"_id": ObjectId(user.user_id)},
        {
            "$set": {
                "first_name": user.first_name,
                "password": hashed_password,
                "updated_datetime": user.updated_datetime,
            }
        },
    )
