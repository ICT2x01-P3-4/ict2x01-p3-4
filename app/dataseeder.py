import bcrypt
from .db import mongo


def insert_car(db):
    """
    Creates a default car object in the database.

    Args:
        db (Database): Database object.
    """
    car_collection = db.car
    car_exist = car_collection.find_one({})

    if not car_exist:
        car_collection.insert_one({
            "distance": 0,
            "is_moving": False,
            "obstacle_detected": False,
        })


def insert_admin(db):
    """
    Creates a default admin user in the database.
    Password will be hashed using bcrypt before inserting.

    Args:
        db (Database): Database object
    """
    user_collection = db.users
    admin_exist = user_collection.find_one({'username': 'admin'})

    if not admin_exist:
        hashed_password = bcrypt.hashpw(
            "P@ssw0rd".encode('utf-8'), bcrypt.gensalt(10))

        user_collection.insert_one({
            "name": "Admin",
            "username": "admin",
            "password": hashed_password,
            "role": "admin"
        })


def insert_user(db):
    collection = db.users
    user_exist = collection.find({'role': 'user'})
    # If the default 3 users not appended, it will seed these data
    if len(list(user_exist)) < 3:
        user1 = {
            'name': 'Audrey',
            'role': 'user',
            'stage': 1,
            'score': 0
        }
        user2 = {
            'name': 'Bobby',
            'role': 'user',
            'stage': 3,
            'score': 30
        }
        user3 = {
            'name': 'Charlie',
            'role': 'user',
            'stage': 2,
            'score': 20
        }
        user_list = [user1, user2, user3]
        collection.insert_many(user_list)


def seed_data():
    """
    Seeds a default car object and an admin user in the database.
    """
    db = mongo.db
    insert_car(db)
    insert_admin(db)
    insert_user(db)
