import os
import re

import requests

baseUrl = "https://drive.google.com/uc?id="

def parse_share_to_download_link(share_link):
    file_id_match = re.search(r'\/d\/(.*?)\/view|\/folders\/(.*)?', share_link)

    if file_id_match:
        file_id = file_id_match.group()
        return f'https://drive.google.com/uc?id={file_id}'
    else:
        raise Exception(f'cant extract ID from {share_link}')

def download_folder(title, link):
    try:
        download_link = parse_share_to_download_link(link);
    except Exception as e:
        print(e)
        return
       
    destination_path = f"output/{title}.zip"

    response = requests.get(download_link)

    if response.status_code == 200:
        with open(destination_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded '{destination_path}' successfully.")
    else:
        raise Exception(f"Failed to download {title}. Status {response.status_code}")

def download_songs(matches):
    os.makedirs('../output', exist_ok=True)

    for match in matches:
        try:
            download_folder(match.title, match.link)
        except Exception as e:
            print(e)
            
def download_exists(title):
    return os.path.isfile(f"output/{title}.zip")


def store_output(matches):
    formatted_matched_songs = ''
    for match in matches:
        formatted_matched_songs += f"{match['name']} by {match['artist']} {match['link']}\n"

    with open("../output.txt", "w") as output_file:
        output_file.write(formatted_matched_songs)
