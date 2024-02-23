import os

import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope='user-library-read'
))


def get_all_liked_songs():
    offset = 0
    limit = 20
    all_liked_songs = []

    while True:
        liked_songs = sp.current_user_saved_tracks(limit, offset)
        if not liked_songs['items']:
            break

        all_liked_songs.extend(liked_songs['items'])
        offset += limit

    return all_liked_songs
