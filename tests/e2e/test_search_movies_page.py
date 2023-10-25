# TODO: Feature 3
from src.repositories.movie_repository import get_movie_repository
from app import app

get_movie_repository().create_movie("test1", "testDirector7", 4)
get_movie_repository().create_movie("test2", "testDirector9", 3)
test_app = app.test_client()

def test_search_movies_with_valid_input():
    
    response = test_app.get('/movies/search?search=test1')
    assert response.status_code == 200
    assert b'Rating: ' in response.data
    assert b'4' in response.data

def test_search_movies_with_invalid_input():
    response = test_app.get('/movies/search?search=nonexistent')
    assert response.status_code == 200
    assert b'Invalid search, try again' in response.data

def test_search_movies_with_no_input():
    response = test_app.get('/movies/search')
    assert response.status_code == 200
    assert b'' in response.data
    