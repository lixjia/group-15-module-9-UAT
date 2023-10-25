# TODO: Feature 1
from flask.testing import FlaskClient
from src.repositories.movie_repository import get_movie_repository
from src.models.movie import Movie

movie_repo = get_movie_repository()
movie_repo.clear_db()

# Sample movies for testing 
movie1 = movie_repo.create_movie("Star Wars", "George Lucas", 4)
movie2 = movie_repo.create_movie("Oppenheimer", "Christopher Nolan", 3)

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

    assert 'Star Wars' in response_data
    assert 'George Lucas' in response_data
    assert '4' in response_data

    assert 'Oppenheimer' in response_data
    assert 'Christopher Nolan' in response_data
    assert '3' in response_data

