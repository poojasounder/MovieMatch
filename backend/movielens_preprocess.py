import pandas as pd

columns = ['movieId', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
           'unknown', 'Action', 'Adventure', 'Animation', 'Children', 'Comedy',
           'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir', 'Horror',
           'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']

movies = pd.read_csv('data/ml-100k/u.item', sep='|', encoding='latin-1', names=columns)

genre_cols = columns[5:]
def genres_to_string(row):
    return '|'.join([genre for genre in genre_cols if row[genre] == 1])

movies['genres'] = movies.apply(genres_to_string, axis=1)
movies = movies[['movieId', 'title', 'genres']]
movies.to_csv('data/movies_ml100k.csv', index=False)
print("Preprocessed dataset saved as movies_ml100k.csv")
