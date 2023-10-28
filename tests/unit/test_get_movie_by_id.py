# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

# Unit test function
def test_get_movie_by_id():
 
     # Set var to movie repo, create a test movie, the the movie ID of test movie,
    movie_repo = get_movie_repository() 
    movie = movie_repo.create_movie("Test Movie Whatever", "Test Director Whatever", 4)
    retrieved_movie = movie_repo.get_movie_by_id(movie.movie_id)

    # Use assert to check the expected outcomes, check if found, check ID, check title, check director check rating
    assert retrieved_movie is not None
    assert retrieved_movie.title == "Test Movie Whatever"
    assert retrieved_movie.director == "Test Director Whatever"
    assert retrieved_movie.rating == 4
