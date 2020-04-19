import numpy as np
import pandas as pd

ratings = pd.read_csv("./ratings.csv")
links = pd.read_csv("./links.csv")
movies = pd.read_csv("./movies.csv")
tags = pd.read_csv("./tags.csv")

######################## NO.1 ###############################
ratings1 = ratings.groupby('userId').aggregate({'rating' : np.median})
max_ratings = ratings1['rating'].max()
min_ratings = ratings1['rating'].min()
max_ratings = ratings1[ratings1['rating'] == max_ratings]
min_ratings = ratings1[ratings1['rating'] == min_ratings]

print('1.최고평점:',end=' ')
size = 0
for idx, row in max_ratings.iterrows() :
    if size == len(max_ratings)-1 :
        print(idx)
    else :
        print(idx, end=',')
        size += 1
print('1.최저평점:',end=' ')
size = 0
for idx, row in min_ratings.iterrows() :
    if size == len(min_ratings)-1 :
        print(idx)
    else :
        print(idx, end=',')
        size += 1
#############################################################
######################## NO.2 ###############################
ratings2 = ratings.groupby('movieId').aggregate({'rating' : np.median})
max_ratings2 = ratings2['rating'].max()
min_ratings2 = ratings2['rating'].min()
max_ratings2 = ratings2[ratings2['rating'] == max_ratings2]
min_ratings2 = ratings2[ratings2['rating'] == min_ratings2]

print('2.최고평점 : ',end=' ')
size = 0
for idx, row in max_ratings2.iterrows() :
    if size == len(max_ratings2)-1 :
        print(movies[movies['movieId'] == idx]['title'].values)
    else :
        print(movies[movies['movieId'] == idx]['title'].values, end=',')
        size += 1
print('2.최저평점 : ',end=' ')
size = 0
for idx, row in min_ratings2.iterrows() :
    if size == len(min_ratings2)-1 :
        print(movies[movies['movieId'] == idx]['title'].values)
    else :
        print(movies[movies['movieId'] == idx]['title'].values, end=',')
        size += 1

#############################################################
######################## NO.3 ###############################
#thriller = (movies['genres'] == 'Thriller') | (movies['genres'] == 'Crime')
thriller = movies[(movies['genres'] == 'Thriller') | (movies['genres'] == 'Crime')]
thriller = pd.merge(ratings, thriller)
#print(thriller)
thriller_ratings = thriller.groupby('movieId').mean()
thriller_ratings = thriller_ratings['rating'].max()
#print(thriller_ratings)
thriller_max = pd.merge(ratings, movies)
#print(thriller_max['rating'])
print('3.범죄스릴러 장르 최고평점 : ',end=' ')
print(thriller_max[thriller_max['rating'] == thriller_ratings]['title'].values)
#############################################################
