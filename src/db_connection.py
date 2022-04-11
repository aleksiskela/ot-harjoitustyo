import sqlite3
from config import DATABASE_FILEPATH

data = sqlite3.connect(DATABASE_FILEPATH)
data.isolation_level = None


def get_db_connection():
    return data
