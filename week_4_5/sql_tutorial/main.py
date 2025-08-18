# imports

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
def insert_user(connection, name:str, age:int, email:str):
    query = "INSERT INTO users (name, age, email) VALUES(?, ?, ?)"
    try:
        with connection:
            connection.execute(query, (name, age, email))
        print(f"User: {name} was added to the database")
    except Exception as e:
        print(e)


# 4 - query all users in the database
def fetch_users(connection, condition: str = None) -> list[tuple]:
    query="SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    try: 
        with connection:
            rows = connection.execute(query).fetchall()
        return rows
    except Exception as e:
        print(e)


# 5 - delete a user from the database
def delete_user(connection, user_id:int):
    query = "DELETE FROM users WHERE id = ?"
    try: 
        with connection:
            connection.execute(query, (user_id, ))
        print(f"USER ID: {user_id} was deleted!")
    except Exception as e:
        print(e)


# 6 - update an existing user
def update_user(connection, user_id:int, email:str):
        query = "UPDATE users SET email = ? WHERE id = ?"
        try:
            with connection:
                connection.execute(query, (user_id, email))
            print(f"USER ID: {user_id} was updated!")
        except Exception as e:
            print(e)

# insert many

def insert_users(connection, users:list[tuple[str, int, str]]):
    query = "INSERT INTO users (name, age, email) VALUES (?,?,?)"
    try: 
        with connection:
            connection.executemany(query, users)
        print(f"{len(users)} users were added")
    except Exception as e:
        print(e)



# main function
def main():
    connection = get_connection("subscribe.db")

    try:
        # create the table
        create_table(connection)

        start = input("Enter Option (Add, Delete, Update, Search, Add Many): ").lower()

        if start == "add":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_user(connection, name, age, email)

        elif start == "search":
            print("All Users:")
            for user in fetch_users(connection):
                print(user)

        elif start == "delete":
            user_id = int(input("Enter USER ID: "))
            delete_user(connection, user_id)

        elif start == "update":
            user_id = int(input("Enter USER ID: "))
            new_email = int(input("Enter new email: "))
            update_user(connection, user_id, new_email)

        elif start == "add many":
            users = [("John", 36, "John@test.com"),
                     ("Fred", 28, "Fred@example.com"),
                     ("Steve", 37, "Steve@example.com"),
                     ("Angela", 20, "Angela@test.com"),
                     ]
            insert_users(connection, users)


    finally:
        connection.close()


if __name__ == "__main__":
    main()
