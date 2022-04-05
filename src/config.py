from dataclasses import dataclass
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "data.db"
DATABASE_FILEPATH = os.path.join(dirname,"..","data",DATABASE_FILENAME)