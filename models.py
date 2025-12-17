class Movie:
    """
   combined rating + movie information
    """

    def __init__(self, movie_id: int, title: str, genres: str):
        self.movie_id = movie_id
        self.title = title
        self.genres = genres.split('|') if genres else []
        self.avg_rating = 0.0
        self.rating_count = 0

    def set_rating_stats(self, avg: float, count: int):
        self.avg_rating = avg
        self.rating_count = count

    def average_rating(self) -> float:
        return self.avg_rating

    def __str__(self) -> str:
        return f"{self.title} | Avg: {self.avg_rating:.2f} ({self.rating_count} ratings)"

    def __lt__(self, other):
        return self.avg_rating < other.avg_rating
