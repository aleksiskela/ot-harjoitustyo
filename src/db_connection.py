import os
import sqlite3

data = sqlite3.connect(f"{os.path.dirname(__file__)}/../data/data.db")
data.isolation_level = None

def get_db_connection():
    return data