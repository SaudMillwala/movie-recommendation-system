"""
defines the RecommendationEngine class which
loads data and generates movie recommendations
"""

import pandas as pd
from models import Movie
from exceptions import DataLoadError


class RecommendationEngine:
    """
    This area is to manage the movies and recommendation logic
    """

    def __init__(self):
        self.movies = {}  

    def load_data(self, movies_path: str, ratings_path: str, min_ratings: int = 50):
        """
        this loads movie data and combines the rating statistics
        """
        try:
            movies_df = pd.read_csv(movies_path)
            ratings_df = pd.read_csv(
                ratings_path,
                usecols=["movieId", "rating"]
            )
        except FileNotFoundError as e:
            raise DataLoadError("CSV file not found") from e

        # creates objects for movie
        for row in movies_df.itertuples(index=False):
            self.movies[row.movieId] = Movie(
                movie_id=row.movieId,
                title=row.title,
                genres=row.genres
            )

        # combines ratings 
        rating_stats = (
            ratings_df
            .groupby("movieId")["rating"]
            .agg(mean="mean", count="count")
            .reset_index()
        )

        # filters movies and attaches a rating
        filtered_movies = {}

        for row in rating_stats.itertuples(index=False):
            movie_id = row.movieId
            avg_rating = row.mean
            rating_count = row.count

            if movie_id in self.movies and rating_count >= min_ratings:
                movie = self.movies[movie_id]
                movie.set_rating_stats(avg_rating, rating_count)
                filtered_movies[movie_id] = movie

        self.movies = filtered_movies


    def movie_generator(self):
        for movie in self.movies.values():
            yield movie

        # adds a rating to the movies
    def recommend_top_movies(self, n: int = 10):
        """
        Recommend top-N movies based on average rating.
        """
        return sorted(
            self.movies.values(),
            key=lambda m: m.average_rating(),
            reverse=True
        )[:n]
