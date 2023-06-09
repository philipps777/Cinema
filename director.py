from validator import Validator

class Director:
    def __init__(self, fullname):
        if not Validator.validate_director(fullname):
            raise ValueError("Invalid director name")

        self.fullname = fullname