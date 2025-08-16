import pickle as pkl
import requests
import pandas as pd
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

movie_dict = pkl.load(open('movies_dict.pkl', 'rb'))
movie_list = pd.DataFrame(movie_dict)
similarity = pkl.load(open('similarity_matrix', 'rb'))

API_KEY = "add your api key here"

# Setup session with retries
session = requests.Session()

# If the TMDb API drops a connection or gives 502 Bad Gateway, Requests will retry automatically without crashing the app.
retry = Retry(
    total=3,  # Retry 3 times
    backoff_factor=1,  # Wait 1s, 2s, 4s between retries
    status_forcelist=[500, 502, 503, 504],
    allowed_methods=["GET"]
)
session.mount('https://', HTTPAdapter(max_retries=retry))


def fetch_poster(movie_id):
    """Fetch movie poster URL from TMDb API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()  # If the status code is 4xx (client error) or 5xx (server error), this will raise an exception
        data = response.json()
        if data.get("poster_path"):
            return "https://image.tmdb.org/t/p/w500" + data["poster_path"]
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching poster for movie {movie_id}: {e}")
    return None  # fallback if fetch fails


def recommend(movie):
    recommended_movies = []
    recommended_movies_posters = []

    # fetch index from movie name
    index = movie_list[movie_list['title'] == movie].index[0]

    distances = similarity[index]

    # The enumerate() function adds a counter and returns pairs of (index, value).
    # We will Sort the movie distances(on actual distance not index) in ascending order (higher the distance more similar) and pick Top 5
    sorted_movies = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Finally will fetch the movie name from the index
    for item in sorted_movies:
        movie_title = movie_list.iloc[item[0]]['title']
        movie_id = movie_list.iloc[item[0]]['id']

        recommended_movies.append(movie_title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters
