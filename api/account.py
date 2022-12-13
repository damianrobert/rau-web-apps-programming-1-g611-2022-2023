import datetime

from api.repository import insert_user, get_user_by_id, delete_user_by_id
from api.users import User


def signup(request_body, connection_string):
    user = User.from_dict(request_body)
    user.created_at = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    user.updated_at = user.created_at

    user.email = user.validate_email()
    user.password = user.validate_password()
    if user.password != user.second_password:
        raise ValueError("Password missmatch.")

    insert_user(user, connection_string)


def signin(request_body, connection_string):
    pass


def update_user(request_body, connection_string):
    pass


def delete_user(user_id, connection_string):
    delete_user_by_id(user_id, connection_string)


def get_user_details(user_id, connection_string):
    user = get_user_by_id(user_id, connection_string)
    return user
