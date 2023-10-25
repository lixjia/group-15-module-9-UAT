from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie
movie_repo = get_movie_repository()
movie1 = movie_repo.create_movie("Star Wars", "George Lucas", 4)
movie2 = movie_repo.create_movie("Oppenheimer", "Christopher Nolan", 3)