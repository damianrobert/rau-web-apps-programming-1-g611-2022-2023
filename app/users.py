import json


class User:
    special_characters = ["*", "?", "!", "#", "&", "=", "(", ")", "_", "-"]

    def __init__(self, id=None, first_name=None, last_name=None,
                 email=None, password=None, second_password=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.second_password = second_password
        self.location = None
        self.balance = 0.0
        self.bio = ""
        self.created_at = None
        self.updated_at = None
        self.last_online = None

        # self.email = self.validate_email()
        # self.password = self.validate_password()

    def validate_email(self):
        email = self.email.lower()
        email = email.replace(" ", "")

        email_parts = email.split("@")

        if len(email_parts) > 2:
            raise ValueError("Email is not formatted correctly. Please try again.")

        second_part = email_parts[1]

        email_ending = second_part.split(".")

        if len(email_ending) > 2:
            raise ValueError("Email is not formatted correctly. Please try again.")

        return email

    def validate_password(self):
        # eliminate spaces
        present_spaces = self.password.find(" ")
        if present_spaces > -1:
            raise ValueError("Invalid password. Password contains spaces.")

        # validate length
        if len(self.password) < 8:
            raise ValueError("Invalid password. Password too short. Minimum 8 characters required.")

        # validate special characters
        present_special = 0
        present_digits = 0
        present_upper = 0
        for character in self.password:
            if character in self.special_characters:
                present_special += 1  # present_special_characters = present_special_characters + 1

            if character.isdigit():
                present_digits += 1

            if character.isupper():
                present_upper += 1

            if present_special and present_digits and present_upper:
                break

        if present_special == 0:
            raise ValueError("Invalid password. Special characters are missing.")

        if present_digits == 0:
            raise ValueError("Invalid password. Missing at least one digit.")

        if present_upper == 0:
            raise ValueError("Invalid password. Missing at least one upper case letter.")

        return self.password

    @classmethod
    def from_dict(cls, user_dict):
        id = user_dict.get("id")
        first_name = user_dict.get("first_name")
        last_name = user_dict.get("last_name")
        email = user_dict.get("email")
        password = user_dict.get("password")
        second_password = user_dict.get("second_password")
        user = cls(id=id, first_name=first_name, last_name=last_name,
                   email=email, password=password, second_password=second_password)
        return user

    @classmethod
    def from_list(cls, user_list):
        id = user_list[0]
        first_name = user_list[1]
        last_name = user_list[2]
        email = user_list[3]
        password = user_list[4]
        second_password = user_list[5]
        user = cls(id=id, first_name=first_name, last_name=last_name,
                   email=email, password=password, second_password=second_password)
        return user

    def to_dict(self):
        user_dict = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "password": self.password,
            "second_password": self.second_password,
            "balance": self.balance,
            "bio": self.bio,
            "location": self.location,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "last_online": self.last_online
        }
        return user_dict

    def to_json(self):
        user_dict = self.to_dict()
        user_json = json.dumps(user_dict)
        return user_json
