import argparse

import chorus
import downloader
import spotify
from track import parse_title
from match import Match

def args():
    parser = argparse.ArgumentParser(
        prog='CloneHeroSpotify',
        description='Helper for getting CH Tracks using your spotify account'
    )
    parser.add_argument('-d', '--download', action='store_true')

    return parser.parse_args()

if __name__ == "__main__":
    args = args()

    download = args.download

    liked_songs = spotify.get_all_liked_songs()
    matches = []

    for song in liked_songs:
        track = song['track']

        name, artist = track['name'], track['artists'][0]['name']

        title = parse_title(name, artist)

        if download and downloader.download_exists(title):
            continue

        match = chorus.search_match(name, artist)
        if match is not None:
            match = Match(title, match['link']);
            matches.append(match)
            print(f"{match.title} found")

    if download:
        downloader.download_songs(matches)
        print(f'successfully downloaded {length(matches)} songs!');
    else:
        downloader.store_output(matches)
        print(f'successfully stored {length(matches)} songs!');

