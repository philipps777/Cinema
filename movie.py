from validator import Validator

class Movie:
  def __init__(self, title, director, year, producer, actors, genre, cinema):
    if not Validator.validate_movie_title(title):
      raise ValueError("Invalid movie title")

    if not Validator.validate_director(director):
      raise ValueError("Invalid director name")

    if not Validator.validate_producer(producer):
      raise ValueError("Invalid producer name")

    if not Validator.validate_year(year):
      raise ValueError("Invalid year")

    if not Validator.validate_actors(actors):
      raise ValueError("Invalid actors")

    if not Validator.validate_genre(genre):
      raise ValueError("Invalid genre")

    if not Validator.validate_cinema(cinema):
      raise ValueError("Invalid cinema")

    self.title = title
    self.director = director
    self.year = year
    self.producer = producer
    self.actors = actors
    self.genre = genre
    self.cinema = cinema


