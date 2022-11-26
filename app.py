import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=4f808e4d7b28853490b7b1677c1304d1&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters


movies_list=pickle.load(open('movies.pkl','rb'))
movies=movies_list
movies_list=movies_list['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))


st.title("Movie Recommender System")
option = st.selectbox(
    'Select the Movie?',
    movies_list)

#if st.button('Recommend'):
 #   rec=recommend(option)
 #   for i in rec:
  #      st.write(i)

if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5,gap="small")
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

