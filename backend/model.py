import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("data/movies_ml100k.csv")
vectorizer = CountVectorizer(tokenizer=lambda x: x.split('|'))
genre_matrix = vectorizer.fit_transform(movies['genres'])
similarity = cosine_similarity(genre_matrix)

def recommend_movies(movie_titles, top_n=5):
    indices = []
    for title in movie_titles:
        matches = movies[movies['title'].str.contains(title, case=False, na=False)]
        if not matches.empty:
            indices.append(matches.index[0])
    if not indices:
        return []

    avg_sim = similarity[indices].mean(axis=0)
    similar_indices = avg_sim.argsort()[::-1]

    recommendations = []
    for idx in similar_indices:
        rec_title = movies.iloc[idx]['title']
        if rec_title not in movie_titles:
            recommendations.append(rec_title)
        if len(recommendations) >= top_n:
            break
    return recommendations
