# Anime Recommendation System

This project provides an anime recommendation system that suggests anime titles based on user preferences, helping viewers find new anime they may enjoy. The system uses data analysis and machine learning to create personalized recommendations, improving the user experience and engagement on streaming platforms.

## Problem Statement
Viewers often spend hours scrolling through a wide variety of anime titles, trying to find something they like. This system aims to make anime recommendations based on user preferences, which can improve the streaming experience and increase time spent on the platform.

## Requirements
To run this project, ensure you have the following libraries installed:

- pandas
- numpy
- matplotlib
- seaborn
- plotly
- wordcloud
- scikit-learn
- pickle
- re

You can install the required packages using pip:
```python
pip install pandas numpy matplotlib seaborn plotly wordcloud scikit-learn
```

## Usage
### 1. Data Analysis
The Jupyter Notebook Anime_Recommendation_System.ipynb is where the data analysis happens. You can run this notebook to explore the anime data, visualize user ratings, anime genre distributions, community size, and more.

- Load data from anime.csv and rating.csv.
- Perform data cleaning and merging.
- Visualize trends, such as top-rated anime and most popular genres.

### 2. Build the Recommendation Model
The system builds a **Nearest Neighbors model** based on user ratings to recommend similar anime titles. There are two main recommendation methods:

- **Collaborative Filtering (KNN):** Recommends anime based on similar user ratings.
- **Content-Based Filtering:** Recommends anime based on genres and textual similarity using a TF-IDF vectorizer and Sigmoid Kernel.

Get recommendations for a specific anime, run the following function:

```python
recommendations = give_rec('Naruto: Shippuuden')
```

This will return the top 10 most similar anime titles to "Naruto: Shippuuden."

### 3. Deploy the Recommendation System
The `app.py` file is a simple web application that serves the recommendation system. You can use Flask or other frameworks to turn this into an API or web-based app.

## Data Analysis and Visualization
The following analyses and visualizations are included in the project:

- **Top 10 Anime Based on Rating Counts:** Shows which anime have the most user ratings.
- **Top 10 Anime Based on Community Size:** Shows the anime with the largest fanbases.
- **Distribution of Ratings:** Displays the distribution of anime ratings from users and websites.
- **Medium of Streaming:** Pie chart showing how different anime are streamed (e.g., TV, web).
- **Genre Word Cloud:** Displays a word cloud of the most common anime genres.
