import streamlit as st
st.set_page_config(page_title='Dsdb',page_icon='🎥')

import pickle
import pandas as pd
import requests
from utils import set_bg

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=c9a903389a732a87c6ab3dbc349242d1&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies= pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommendation System')


movie_list = movies['title'].values
st.text("Can't decide what to watch?")
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendations'):
    names,posters = recommend(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

set_bg('Background.jpg')

st.title("The Smart Way To Pick A Movie")

st.text("Watching movies on weekends is fun, but figuring out what to watch is irritating.")
st.text("Endlessly scrolling through YouTube, Netfilx, Wasting an hour and still not ")
st.text( "decided what to watch-we have been there right?")
st.text("Then you landed at right place!")
st.text("Dsdb movie recommendation engine is the answer to the question ")
st.text("What movie should I watch?")
