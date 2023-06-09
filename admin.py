from user import User
from validator import Validator
from movie import Movie
from base_repository import BaseRepository


class Admin:
    def __init__(self, user: User):
        if Validator.validate_admin(user):
            raise ValueError("Invalid user object")

        self.user = user

    def create_movie(self, title, director, year, producer, actors, genre, cinema):

        movie = Movie(title, director, year, producer, actors, genre, cinema)

        BaseRepository.movies.append(movie)

    def update_movie(self, oldMovieTitle: str, newMovie: Movie):
        is_found = False
        for index, movie in enumerate(BaseRepository.movies):
            if movie.title == oldMovieTitle:
                BaseRepository.movies[index] = newMovie
                is_found = True
                break
        if not is_found:
            title, director, year, producer, actors, genre, cinema = \
                newMovie.title, newMovie.director, newMovie.year, newMovie.producer, newMovie.actors, newMovie.genre, newMovie.cinema
            self.create_movie(title, director, year, producer, actors, genre, cinema)


    def delete_movie(self, title):
        for index, movie in enumerate(BaseRepository.movies):
            if movie.title == title:
                BaseRepository.movies.remove(BaseRepository.movies[index])
                break

    def update_cinema(self, cinema):
        for movie in BaseRepository.movies:
            movie.cinema = cinema

    def delete_cinema(self):
        BaseRepository.movies.clear()


    # def create_cinema(self, name, address, schedule):
    #     cinema = Cinema(name, address, schedule)
    #     self.schedule.append(cinema)



# delite_movie
# create_cinema