import numpy as np
import pandas as pd

top_left = pd.read_csv('pandas/top1-25-1.csv')
top_right = pd.read_csv('pandas/top1-25-2.csv')
bottom_left = pd.read_csv('pandas/top26-50-1.csv')
bottom_right = pd.read_csv('pandas/top26-50-2.csv')

top = pd.merge(top_left, top_right, on='Track.Name')

bottom = pd.concat([bottom_left, bottom_right], axis=1)

df = pd.concat([top, bottom], sort=False)

df['#'] = list(range(1, 51))
df.set_index('#', inplace=True)

# genre = df.groupby('Genre')

# df = genre.count()
# print(df[df['Energy'] > 3]['Energy'])

# most_popular_number = genre['Popularity'].mean().max()
# most_popular_genre = genre['Popularity'].mean().idxmax()
# least_popular_number = genre['Popularity'].mean().min()
# least_popular_genre = genre['Popularity'].mean().idxmin()

# print(most_popular_genre, most_popular_number)
# print(least_popular_genre, least_popular_number)

# cols = df.columns.tolist()[3:]
# genres = genre[cols].mean().idxmax()
# numbers = genre[cols].mean().max()
# result = pd.DataFrame([cols, genres, numbers], ['Indikatorius', 'Žanras', 'Balai']).transpose()
# print(result)

print(df.info())
print(df[df['Genre'].isnull() | df['Popularity'].isnull()])
df['Genre'] = df['Genre'].fillna('pop')
df['Popularity'] = df['Popularity'].fillna(value=df['Popularity'].mean())
print(df.head())