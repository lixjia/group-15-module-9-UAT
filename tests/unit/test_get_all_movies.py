from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repo = get_movie_repository()
movie_repo.clear_db()

# Sample movies to for testing 
movie1 = movie_repo.create_movie("Star Wars", "George Lucas", 4)
movie2 = movie_repo.create_movie("Oppenheimer", "Christopher Nolan", 3)

# Correct dictionary
correct_movies = {
    movie1.movie_id: movie1,
    movie2.movie_id: movie2
}

def test_get_all_movies():
    movie_repo = get_movie_repository()
    all_movies = movie_repo.get_all_movies()

    # Verify that get_all_movies() returns ALL movies, len should match the number of created movies
    assert len(all_movies) == 2

    # Makes sure it returns a dictionary
    assert isinstance(all_movies, dict)

    # Checks that get_all_movies() returns a correct dictionary
    assert all_movies == correct_movies


