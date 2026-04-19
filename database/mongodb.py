import os
import logging
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

logger = logging.getLogger(__name__)

MONGO_URI = os.environ.get("MONGO_URI", "")

_client = None
_db = None


def get_client():
    global _client
    if _client is None and MONGO_URI:
        try:
            _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            _client.admin.command("ping")
            logger.info("MongoDB connected.")
        except ConnectionFailure as e:
            logger.warning(f"MongoDB connection failed: {e}. Running without DB.")
            _client = None
    return _client


def get_db(db_name="teletips"):
    global _db
    client = get_client()
    if client is not None:
        _db = client[db_name]
    return _db


def add_user(user_id, username=None, full_name=None):
    db = get_db()
    if db is None:
        return
    db["users"].update_one(
        {"_id": user_id},
        {"$set": {"username": username, "full_name": full_name}},
        upsert=True,
    )


def get_user(user_id):
    db = get_db()
    if db is None:
        return None
    return db["users"].find_one({"_id": user_id})


def get_all_users():
    db = get_db()
    if db is None:
        return []
    return list(db["users"].find({}, {"_id": 1}))


def total_users():
    db = get_db()
    if db is None:
        return 0
    return db["users"].count_documents({})


def increment_upload(user_id):
    db = get_db()
    if db is None:
        return
    db["users"].update_one(
        {"_id": user_id},
        {"$inc": {"uploads": 1}},
        upsert=True,
    )


def get_upload_count(user_id):
    db = get_db()
    if db is None:
        return 0
    doc = db["users"].find_one({"_id": user_id}, {"uploads": 1})
    return doc.get("uploads", 0) if doc else 0


def total_uploads():
    db = get_db()
    if db is None:
        return 0
    pipeline = [{"$group": {"_id": None, "total": {"$sum": "$uploads"}}}]
    result = list(db["users"].aggregate(pipeline))
    return result[0]["total"] if result else 0
