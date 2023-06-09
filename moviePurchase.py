from validator import Validator

class MoviePurchase:

    def __init__(self, username, movie_title, purchase_date):

        if not Validator.validate_username(username):
            raise ValueError("Invalid username")


        if not Validator.validate_movie_title(movie_title):
            raise ValueError("Invalid movie_title")

        if not Validator.validate_movie_purchase_date(purchase_date):
            raise ValueError("Invalid movie_purchase_date")


        self.username = username
        self.movie_title = movie_title
        self.purchase_date = purchase_date