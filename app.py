import pickle
import streamlit as st

def recommend(anime):
    index = animes[animes['name'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_anime_names = []
    for i in distances[1:6]:
        recommend_anime_names.append(animes.iloc[i[0]].name)

    return recommend_anime_names

page_bg_img = '''
<style>
      .stApp {
  background-image: url("https://wallpapercave.com/dwp2x/wp6416633.jpg");
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)


st.markdown('# Anime Recommendation System')
animes = pickle.load(open('anime_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

anime_list = animes['name'].values
selected_anime = st.selectbox(
    "Type or select a movie from the dropdown",
    anime_list
)


if st.button('Show Recommendation'):
    recommended_anime_names = recommend(selected_anime)
    for i in recommended_anime_names:
        st.subheader(i)