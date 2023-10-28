# TODO: Feature 4
from app import app
from src.repositories.movie_repository import get_movie_repository

#Create test client
test_app = app.test_client()

# Test if the page will load
def test_get_single_movie():
	
	# Simulate a GET request
	response = test_app.get('movies/search')
	# Check if the HTTP status code is 200, 'aka' sucessful
	assert response.status == '200 OK'
