import sqlite3

from api.users import User

# TODO: change this path to match the path to your db file.
# CONNECTION_STRING = "/Users/luchicila/Work/RAU/rau-web-apps-programming-1-g611-2022-2023/datastore/datastore.db"
CONNECTION_STRING = r'C:\Users\Damian\OneDrive - UNIVERSITATEA ROMANO-AMERICANA\FACULTATE\AN II\Aplicatii Web\Aplicatie_Web_Seminar\rau-web-apps-programming-1-g611-2022-2023\datastore\datastore.db'


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

    try:
        # execute query
        cursor.execute(query)

        # commit
        conn.commit()

        # close connection
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        raise e


def get_all_users(connection_string):
    conn = sqlite3.connect(connection_string)

    query = "select * from users;"

    cursor = conn.cursor()

    try:
        entries = list(cursor.execute(query))
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        raise e

    users = []
    for entry in entries:
        user = User.from_list(entry)
        users.append(user)

    return users


def get_user_by_email(user, connection_string):
    query = f"select * from users where email = '{user.email}'";

    conn = sqlite3.connect(connection_string)
    cursor = conn.cursor()
    try:
        entries = cursor.execute(query)
        user = entries.fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        raise e

    existing_user = User.from_list(user)
    return existing_user


def get_user_by_id(user_id, connection_string):
    query = f"SELECT * FROM users WHERE id = {user_id};"
    conn = sqlite3.connect(connection_string)
    cursor = conn.cursor()
    try:
        data = cursor.execute(query).fetchone()
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        raise e

    user = User.from_list(data)
    return user


def delete_user_by_id(user_id, connection_string):
    query = f"DELETE FROM users WHERE id = {user_id};"
    conn = sqlite3.connect(connection_string)
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        cursor.close()
        conn.close()
        raise e