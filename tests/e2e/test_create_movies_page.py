from src.repositories.movie_repository import get_movie_repository
from app import app

test_app = app.test_client()

def test_create_movie_with_valid_input():
    # Simulate a form submission with valid input
    response = test_app.post('/movies', data=dict(title='New Movie', director='New Director', rating=5))

    # After creating the movie, the response should be a redirect to the list all movies page
    assert response.status_code == 302
    assert response.location.endswith('/movies')

    # Check if the newly created movie appears in the search results
    search_response = test_app.get('/movies/search?search=New Movie')
    assert search_response.status_code == 200
    assert b'Rating' in search_response.data
    assert b'5' in search_response.data

def test_create_movie_with_invalid_input():
    # Simulate a form submission with invalid input
    response = test_app.post('/movies', data=dict(title='', director='', rating=6))

    # After an invalid submission, the page should reload with errors
    assert response.status_code == 302
