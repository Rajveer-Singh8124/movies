import streamlit as st
from pickle import load
import pandas as pd 

@st.cache_data
def data():
    movie_dict = load(open("movies_dict.pkl","rb"))
    similarity = load(open("similarity.pkl","rb"))
    return movie_dict,similarity


def recommend(movie):
    idx = movies[movies.title == movie].index[0]
    distance = similarity[idx]
    
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x:x[1])[0:5]

    recommended_movies = []


    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        
    return recommended_movies


movie_dict,similarity = data()
movies = pd.DataFrame(movie_dict)

#  custom css
with open("style.css") as css:
    st.markdown(f"<style>{css.read()}</style>",unsafe_allow_html=True)



st.title("MOVIES")
movieName =  st.selectbox(f'Total movies {len(movies["title"].values)}',(movies["title"].values))

if st.button("Recommend"):
    name = recommend(movieName)


    col1,col2,col3,col4,col5 =st.columns(5)
    with col1:
        st.write(name[0])
    with col2:
        st.write(name[1])   
    with col3:
        st.write(name[2])
    with col4:
        st.write(name[3])
    with col5:
        st.write(name[4])
