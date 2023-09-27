import argparse

import chorus
import downloader
import spotify
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
        title = name + " - " + artist

        if downloader.download_exists(title):
            continue

        match = chorus.search_match(name, artist)
        if match is not None:
            match = Match(title, match['link']);
            matches.append(match)
            print(match.title)

    if download:
        downloader.download_songs(matches)
    else:
        downloader.store_output(matches)
