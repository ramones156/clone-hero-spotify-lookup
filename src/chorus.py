import json

import requests

from match import Match

url = "https://api.enchor.us/search/advanced"

cached_matches_path = '../data.json'
cached_matches = []


def find_match(name, artist):
    # global cached_matches
    # if cached_matches.__len__() == 0:
    #     if Path(cached_matches_path).is_file():
    #         with open(cached_matches_path) as f:
    #             cached_matches = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    #
    # title = parse_title(name, artist)
    # return cached_matches.get(title, None)
    return search_match(name, artist)


def search_match(name, artist):
    body = {
        "instrument": None,
        "difficulty": None,
        "name": {
            "value": name,
            "exact": True,
            "exclude": False
        },
        "artist": {
            "value": artist,
            "exact": True,
            "exclude": False
        },
        "album": {
            "value": "",
            "exact": False,
            "exclude": False
        },
        "genre": {
            "value": "",
            "exact": False,
            "exclude": False
        },
        "year": {
            "value": "",
            "exact": False,
            "exclude": False
        },
        "charter": {
            "value": "",
            "exact": False,
            "exclude": False
        },
        "minLength": None,
        "maxLength": None,
        "minIntensity": None,
        "maxIntensity": None,
        "minAverageNPS": None,
        "maxAverageNPS": None,
        "minMaxNPS": None,
        "maxMaxNPS": None,
        "modifiedAfter": "",
        "hash": "",
        "hasSoloSections": None,
        "hasForcedNotes": None,
        "hasOpenNotes": None,
        "hasTapNotes": None,
        "hasLyrics": None,
        "hasVocals": None,
        "hasRollLanes": None,
        "has2xKick": None,
        "hasIssues": None,
        "hasVideoBackground": None,
        "modchart": None
    }

    response = requests.post(url, json=body)

    if response.status_code != 201:
        print(response.content)
        response.raise_for_status()

    content = response.json()

    songs = content['data']
    if len(songs) <= 0:
        return None

    song = songs[0]

    if name not in song['name'] or artist not in song['artist']:
        return None

    return song


def store_matches(matches: [Match]):
    with open(cached_matches_path, 'w') as f:
        json.dump(matches, f)
