import streamlit as st
from utils import recommend, movie_list

st.title('Movies Recommender System')

selected_movie = st.selectbox(
    "Select a movie",
    (movie_list['title'].values),
)

names, posters = recommend(selected_movie)
if st.button('Get Recommendation', type="primary"):
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(names[0])
        st.image(posters[0])

    with col2:
        st.header(names[1])
        st.image(posters[1])

    with col3:
        st.header(names[2])
        st.image(posters[2])

    with col4:
        st.header(names[3])
        st.image(posters[3])

    with col5:
        st.header(names[4])
        st.image(posters[4])
