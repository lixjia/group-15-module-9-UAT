from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

from flask import Flask, redirect, render_template, request
from random import randint

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

# Uncomment for manual creation, unecessary when feature 2 complete:
# movie_repository.create_movie("Star Wars", "George Lucas", 4)
# movie_repository.create_movie("Oppenheimer", "Christopher Nolan", 3)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_list = get_movie_repository().get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movie_list=movie_list)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    # Get data from the form submission
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])

    # Add the new movie to the movie repository
    movie_repository.create_movie(title, director, rating)

    # After creating the movie in the database, redirect to the list all movies page
    return redirect('/movies')

@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    # get_movie_repository().create_movie("test1", "testDirector", 4)
    # get_movie_repository().create_movie("test2", "testDirector", 3)
    name = request.args.get('search')
    movie = get_movie_repository().get_movie_by_title(name)
    title = ''
    error = ''
    
    if(name == None):
        error = ''
        title = ''
    elif(movie == None):
        error = "Invalid search, try again"
    else:
        title = 'Rating: '
        error = ''
    
    return render_template('search_movies.html', search_active=True, movie=movie, error=error, title=title)
    
    
        
    


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    return render_template('get_single_movie.html')


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    return render_template('edit_movies_form.html')


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    # TODO: Feature 5
    # After updating the movie in the database, we redirect back to that single movie page
    return redirect(f'/movies/{movie_id}')


@app.post('/movies/<int:movie_id>/delete')
def delete_movie(movie_id: int):
    # TODO: Feature 6
    pass

if __name__ == '__main__':
    app.run()