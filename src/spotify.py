from dotenv import load_dotenv

load_dotenv()
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope='user-library-read'
))


def get_all_liked_songs():
    offset = 0
    all_liked_songs = []

    while True:
        liked_songs = sp.current_user_saved_tracks(offset=offset)
        if not liked_songs['items']:
            break
        all_liked_songs.extend(liked_songs['items'])
        offset += len(liked_songs['items'])

    return all_liked_songs
