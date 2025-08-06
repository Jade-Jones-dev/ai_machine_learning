#imports

import sqlite3
from icecream import ic as print

# one way to connect
# connection = sqlite3.connect("subscribe.db")
# cursor = connection.cursor()
# cursor.execute()
# connection.close()

# 1 - setup/ initialize database
def get_connection(db_name):
    try:
        return sqlite3.connect(db_name)
    except Exception as e:
        print(f"Error: {e}")
        raise


# 2 - create a table in the database
def create_table(connection):
    query = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
    )
"""
    try:
        with connection:
            connection.execute(query)
        print("Table was created")
    except Exception as e:
        print(e)



# 3 - add a user to the database

# 4 - query all users in the database

# 5 - delete a user from the database

# 6 - update an existing user

# main function
def main():
    connection = get_connection("subscribe.db")

    #create the table
    create_table(connection)



if __name__ == "__main__":
    main()