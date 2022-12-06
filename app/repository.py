import sqlite3

from app.users import User


def insert_user(user, connection_string):
    # connect to database
    conn = sqlite3.connect(connection_string)

    # create query
    query = f"""insert into users(
        first_name, 
        last_name, 
        email, 
        password, 
        second_password, 
        created_at, 
        updated_at
    )
    values (
        '{user.first_name}', 
        '{user.last_name}', 
        '{user.email}', 
        '{user.password}', 
        '{user.second_password}',
        '{user.created_at}',
        '{user.updated_at}'
    );"""

    # create cursor
    cursor = conn.cursor()

    # execute query
    cursor.execute(query)

    # commit
    conn.commit()

    # close connection
    cursor.close()
    conn.close()


def get_all_users(connection_string):
    conn = sqlite3.connect(connection_string)

    query = "select * from users;"

    cursor = conn.cursor()

    entries = list(cursor.execute(query))

    conn.close()

    users = []
    for entry in entries:
        user = User.from_list(entry)
        users.append(user)

    return users


def get_user_by_email(user, connection_string):
    query = f"select * from users where email = '{user.email}'";

    conn = sqlite3.connect(connection_string)
    cursor = conn.cursor()
    entries = cursor.execute(query)
    user = entries.fetchone()
    conn.close()

    existing_user = User.from_list(user)
    return existing_user
