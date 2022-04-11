from db_connection import get_db_connection


def init_db():
    database = get_db_connection()
    drop_existing_tables(database)
    create_tables(database)


def drop_existing_tables(database):
    database.execute("DROP TABLE IF EXISTS Storages")
    database.execute("DROP TABLE IF EXISTS Items")


def create_tables(database):
    database.execute(
        "CREATE TABLE Storages (id INTEGER PRIMARY KEY, name TEXT)")
    database.execute("""CREATE TABLE Items (id INTEGER PRIMARY KEY,
storage_id INTEGER REFERENCES Storages, item_name TEXT, amount INTEGER DEFAULT 0,
minimum_amount INTEGER)""")


if __name__ == "__main__":
    init_db()
