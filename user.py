from validator import Validator

class User:
    def __init__(self, username, password, role):

        if not Validator.validate_username(username):
            raise ValueError("Invalid username")

        if not Validator.validate_password(password):
            raise ValueError("Invalid password")

        if not Validator.validate_role(role):
            raise ValueError("Invalid role")

        self.username = username
        self.password = password
        self.role = role
