import pandas as pd
import numpy as np
import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key = lambda x:x[1])[1:7]
    
    recommend_movies = []

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


st.title('Movie Recommender System')
selected_movie_name = st.selectbox(
    "Movie Name",
    movies['title'].values
)
if st.button("Recommend"):
    Recommendations = recommend(selected_movie_name)
    for i in Recommendations:
        st.write(i)