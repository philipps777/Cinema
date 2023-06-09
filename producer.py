from validator import Validator

class Producer:
    def __init__(self, fullname):
        if not Validator.validate_producer(fullname):
            raise ValueError("Invalid producer name")

        self.fullname = fullname

