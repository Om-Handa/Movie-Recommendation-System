import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

movies = pickle.load(open("movies.pkl", "rb"))

tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = tfidf.fit_transform(
    movies["tags"]
)

similarity = cosine_similarity(vectors)

def recommend(movie):

    movie_index = movies[
        movies['title'] == movie
    ].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in distances:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


st.markdown("""
<h1 style='text-align:center;color:#ff4b4b'>
🎬 Movie Recommendation System
</h1>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center'>Find movies similar to your favorites using TF-IDF and Cosine Similarity</p>",
    unsafe_allow_html=True
)

st.divider()

selected_movie = st.selectbox(
    "🎥 Select a Movie",
    movies["title"].values
)

if st.button("Recommend Movies", use_container_width=True):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    cols = st.columns(5)

    for idx, movie in enumerate(recommendations):

        with cols[idx]:

            st.markdown(
                f"""
                <div style="
                    padding:20px;
                    border-radius:15px;
                    background:#262730;
                    text-align:center;
                    height:150px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-weight:bold;
                ">
                    {movie}
                </div>
                """,
                unsafe_allow_html=True
            )