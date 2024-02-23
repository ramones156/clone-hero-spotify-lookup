import os

import requests

from match import Match

baseUrl = "https://www.enchor.us/download"


def download_folder(match: Match):
    params = {
        'md5': match.md5,
        'filename': match.filename,
        'isSng': False,
    }
    response = requests.get(baseUrl, params)

    if response.status_code != 200:
        raise Exception(f"Failed to download {match.title}. Status {response.status_code}")

    destination_path = f"../output/{match.title}.zip"

    with open(destination_path, 'xb') as f:
        f.write(response.content)

    print(f"Downloaded '{destination_path}' successfully.")


def download_songs(matches):
    os.makedirs('../output', exist_ok=True)

    for match in matches:
        try:
            download_folder(match)
        except Exception as e:
            print(e)


def download_exists(title):
    return os.path.isfile(f"output/{title}.zip")


def store_output(matches):
    formatted_matched_songs = ''
    for match in matches:
        formatted_matched_songs += f"{match['name']} by {match['artist']} {match['driveId']}\n"

    with open("../output.txt", "w") as output_file:
        output_file.write(formatted_matched_songs)
