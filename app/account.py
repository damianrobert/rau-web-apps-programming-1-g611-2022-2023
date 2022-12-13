import datetime

from app.repository import insert_user
from app.users import User


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


def delete_user(request_body, connection_string):
    pass


def get_user_details(request_body, connection_string):
    pass
