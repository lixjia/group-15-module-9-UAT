from src.repositories.movie_repository import get_movie_repository
get_movie_repository().clear_db()
get_movie_repository().create_movie("test1", "testDirector7", 4)
get_movie_repository().create_movie("test2", "testDirector9", 3)

def test_get_title():
    
    #test the size
    assert len(get_movie_repository().get_all_movies()) == 2
    #test that it matches director with a known movie
    assert get_movie_repository().get_movie_by_title('test1').director == 'testDirector7'
    #test that no movie exist
    assert get_movie_repository().get_movie_by_title('test4') == None
    
    
    