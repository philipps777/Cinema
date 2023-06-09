from user import User
import datetime
from cinema import Cinema
from movie import Movie


class Validator:
    @staticmethod
    def validate_movie_title(title):
        if not isinstance(title, str) or not title:
            return False
        return True

    @staticmethod
    def validate_director(director):
        if not isinstance(director, str) or not director:
            return False
        return True

    @staticmethod
    def validate_year(year):
        if not isinstance(year, int) or datetime.datetime.now().year < year < 1900:
            return False

        return True

    @staticmethod
    def validate_producer(producer):
        if not isinstance(producer, str) or not producer:
            return False
        return True

    @staticmethod
    def validate_actors(actors):
        if not isinstance(actors, list) or not all(isinstance(actor, str) for actor in actors):
            return False
        return True

    @staticmethod
    def validate_genre(genre):
        genres = ["Action", "Comedy", "Drama", "Fantasy", "Horror", "Romance", "Thriller"]
        return genre in genres

    @staticmethod
    def validate_admin(admin):
        if not isinstance(admin, User):
            return False
        return True

    @staticmethod
    def validate_cinema(cinema):
        if not isinstance(cinema, Cinema):
            return False
        return True

    @staticmethod
    def validate_movie(movie):
        if not isinstance(movie, Movie):
            return False
        return True

    @staticmethod
    def validate_cinema_name(name):
        if not isinstance(name, str) or not name:
            return False
        return True

    @staticmethod
    def validate_cinema_address(address):
        if not isinstance(address, str) or not address:
            return False
        return True

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str) or not username:
            return False
        return True

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str) or not password:
            return False
        return True

    @staticmethod
    def validate_role(role):
        person = ["admin", "user"]

        return role in person

    @staticmethod
    def validate_movie_purchase_date(purchase_date):
        if not isinstance(purchase_date, datetime.date):
            return False
        return True


