# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from app import app

get_movie_repository().clear_db()

# Sample movies for testing 
get_movie_repository().create_movie("test1", "testDirector7", 4)
get_movie_repository().create_movie("test2", "testDirector9", 3)

def test_list_all_movies(test_app: FlaskClient):
    response = test_app.get('/movies')
    assert response.status_code == 200
    response_data = response.data.decode('utf-8')

    assert '<h1 class="mb-5">All Movies</h1>' in response_data
    assert '<p class="mb-3">See our list of movie ratings below</p>' in response_data

    # Make sure the table has all headers present
    assert '<th scope ="col">ID</th>' in response_data
    assert '<th scope="col">Name</th>' in response_data
    assert '<th scope="col">Director</th>' in response_data
    assert '<th scope="col">Rating</th>' in response_data

    # Makes sure correct test movie data is in table
    assert 'test1' in response_data
    assert 'testDirector7' in response_data
    assert '4' in response_data
    assert 'test2' in response_data
    assert 'testDirector9' in response_data
    assert '3' in response_data
