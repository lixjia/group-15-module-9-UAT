from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

get_movie_repository().clear_db()

# Sample movies to for testing 
movie1 = get_movie_repository().create_movie("Star Wars", "George Lucas", 4)
movie2 = get_movie_repository().create_movie("Oppenheimer", "Christopher Nolan", 3)

# Dictionary with correct values
correct_movies = {
    movie1.movie_id: movie1,
    movie2.movie_id: movie2
}

def test_get_all_movies():
    # Makes sure it returns a dictionary
    assert isinstance(get_movie_repository().get_all_movies(), dict)

    # Makes sure the dictionary created by get_all_movies() has the correct data (is the same as the correct_movies dict)
    dictionaries_match = True
    for key, value in correct_movies.items():
        if key not in get_movie_repository().get_all_movies() or get_movie_repository().get_all_movies()[key] != value:
            all_data = False
            break
    assert dictionaries_match
