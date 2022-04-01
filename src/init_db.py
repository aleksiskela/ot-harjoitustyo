from db_connection import get_db_connection

def init_db():
    database = get_db_connection()
    drop_existing_tables(database)
    create_tables(database)

def drop_existing_tables(database):
    try:
        database.execute("drop table Storages")
    except:
        pass
    try:
        database.execute("drop table Items")
    except:
        pass

def create_tables(database):
    database.execute("create table Storages (id integer primary key, name text)")
    database.execute("create table Items (id integer primary key, item_name text, amount integer)")

if __name__=="__main__":
    init_db()