import requests

baseUrl = "https://chorus.fightthe.pw/api/search?query="

def search_match(name, artist):
    url = baseUrl + "name=\""+name+"\" artist=\""+artist+"\"" # dont ask why
  
    response = requests.get(url)

    if response.status_code != 200:
        response.raise_for_status()

    content = response.json();

    songs = content['songs']
    if len(songs) <= 0:
        return None
  
    song = songs[0]
  
    if name not in song['name'] or artist not in song['artist']:
        return None

    return song
