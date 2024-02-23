import argparse
from time import sleep
import json

import chorus
import downloader
import spotify

from match import Match
from track import parse_title


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

        match = chorus.find_match(name, artist)
        if match is not None:
            match = Match(title, match['driveFileName'], match['md5'])
            matches.append(match)
            print(f"{match.title} found")

        sleep(0.4)  # TMR

    # store matches
    # chorus.store_matches(matches)

    if download:
        downloader.download_songs(matches)
        print(f'successfully downloaded {len(matches)} songs!')
    else:
        downloader.store_output(matches)
        print(f'successfully stored {len(matches)} songs!')
