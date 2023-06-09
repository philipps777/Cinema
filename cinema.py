from validator import Validator

class Cinema:


    def __init__(self, name, address):

        if not Validator.validate_cinema_name(name):
            raise ValueError("Invalid name")

        if not Validator.validate_cinema_address(address):
            raise ValueError("Invalid address")

        self.name = name
        self.address = address
    #     self.schedule = []
    #
    # def add_movie_to_schedule(self, movie, time):
    #     self.schedule.append((movie, time))

