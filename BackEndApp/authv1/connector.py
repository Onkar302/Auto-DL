import os
import pymongo
from dotenv import load_dotenv

load_dotenv()


def connect(db_name="auth_db"):
    """
    Connect to mongodb instance (url) in .env file.

    Parameter
    ----------
    db_name : str
        name of the database to connect

    Returns
    ---------
    db : object
        database client connection object
    """
    client = pymongo.MongoClient(os.getenv("HOST"))
    db = client[db_name]
    print("MongoDB connected")
    return db


if __name__ == "__main__":
    db = connect()
