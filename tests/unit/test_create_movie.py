# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

# Get the movie repository singleton to use throughout the test
movie_repository = get_movie_repository()

def test_create_movie():
    # Arrange
    initial_movie_count = len(movie_repository.get_all_movies())
    title = "Test Movie"
    director = "Test Director"
    rating = 5

    # Act
    created_movie = movie_repository.create_movie(title, director, rating)
    movies_after_creation = movie_repository.get_all_movies()

    # Assert
    assert created_movie is not None
    assert created_movie.title == title
    assert created_movie.director == director
    assert created_movie.rating == rating
    assert len(movies_after_creation) == initial_movie_count + 1
    assert created_movie in movies_after_creation.values()
