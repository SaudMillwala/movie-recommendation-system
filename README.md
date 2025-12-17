# Movie Recommendation and Rating Analysis System

## Course
AAI / CPE / EE 551

## Team Members
- Saud Millwala (smillwal@stevens.edu)
- Preksha Shah (pshah12@stevens.edu)

## Problem Description

With the rapid growth of online streaming platforms such as Netflix, Amazon Prime, and Disney+, users are exposed to thousands of movies. This abundance of choices often makes it difficult for users to decide what to watch next.

The goal of this project is to design and implement a movie recommendation system that helps the user discover high quality movies using historical rating data. By analyzing movie ratings and genres, the system generates meaningful recommendations and provides insights into overall rating trends.

## Dataset

This project uses the publicly available MovieLens 20M dataset provided by GroupLens.  
The dataset contains approximately 20 million movie ratings created by over 138,000 users across more than 27,000 movies.

The following files are used:
- `movies.csv`: Movie titles and genres
- `ratings.csv`: User ratings for movies

To improve recommendation performance, movies with fewer than 50 ratings are filtered out during data loading.

## Program Structure

- `main.ipynb`  
  Runs the recommendation system, displays recommendations, and generates visualizations

- `engine.py`  
  Contains the RecommendationEngine class, which loads data and implements recommendation logic

- `models.py`  
  Defines the Movie class and stores movie related attributes and methods.

- `plots.py`  
  Generates visualizations such as rating distributions and top rated movies using Matplotlib

- `tests/test_engine.py`  
  Contains unit tests written using Pytest to validate the recommendation functionality

- `data/`  
  Stores the MovieLens CSV dataset files

## Features Implemented

- Popularity based movie recommendations using average ratings
- Genre-based movie recommendations
- Efficient data processing using Pandas
- Data visualization using Matplotlib
- Object oriented design with multiple classes
- Exception handling for data loading
- Unit testing using Pytest

## How to Run the Program

1. Install required libraries:
   ```bash
   pip install pandas matplotlib pytest
   pip install -r requirements.txt

2. Launch Jupyter Notebook and run

    jupyter notebook main.ipynb

3. Run all cells to load data, generate recommendations, and display plots

## Team Contributions

## Team Contributions

Both team members collaborated closely on the design, implementation, and testing of the movie recommendation system.

- Saud Millwala:
  - Focused on test enigne and performance improvements
  - Implemented visualization components
  - Collaborated on recommendation engine and logic
  - Collaborated in documentation

- Preksha Shah:
  - Focused on recommendation methodology and data processing logic
  - Collaborated on recommendation engine and logic
  - Collaborated in documentation
  - Focused on Data optimization
