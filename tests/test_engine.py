import pytest
from engine import RecommendationEngine


@pytest.fixture
def engine():
    """
    this automatically runs the RecommendationEngine loaded with movie and rating data
    """
    eng = RecommendationEngine()
    eng.load_data("data/movies.csv", "data/ratings.csv")
    return eng


def test_recommend_top_movies_length(engine):
    """
    this tests to see if recommend_top_movies returns the correct number of movies
    """
    results = engine.recommend_top_movies(5)
    assert len(results) == 5


def test_recommend_by_genre(engine):
    """
    this checks if recommend_by_genre returns movies only from the specified genre
    """
    results = engine.recommend_by_genre("Action", 5)
    assert len(results) > 0

    for movie in results:
        assert "Action" in movie.genres
