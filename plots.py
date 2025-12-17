import matplotlib.pyplot as plt

#this is used to plot the avg distribution of the ratings
def plot_rating_distribution(movies):
    ratings = [m.average_rating() for m in movies if m.rating_count > 0]

    plt.figure()
    plt.hist(ratings, bins=20)
    plt.title("Distribution of Average Movie Ratings")
    plt.xlabel("Average Rating")
    plt.ylabel("Number of Movies")
    plt.show()

#This plots the top movies
def plot_top_movies(movies, n=10):
    top_movies = sorted(
        movies,
        key=lambda m: m.average_rating(),
        reverse=True
    )[:n]

    titles = [m.title for m in top_movies]
    ratings = [m.average_rating() for m in top_movies]

    plt.figure()
    plt.barh(titles, ratings)
    plt.xlabel("Average Rating")
    plt.title(f"Top {n} Movies by Rating")
    plt.gca().invert_yaxis()
    plt.show()
