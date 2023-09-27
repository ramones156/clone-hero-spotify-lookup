import spotify
import chorus

if __name__ == "__main__":
    liked_songs = spotify.get_all_liked_songs()
    matched_songs = []

    for song in liked_songs:
        track = song['track']
        name, artist = track['name'], track['artists'][0]['name']

        match = chorus.search_match(name, artist)
        if match is not None:
            formatted_match = f"{match['name']} by {match['artist']} {match['link']}"
            matched_songs.append(formatted_match)
            print(formatted_match)

    formatted_matched_songs = '\n'.join(matched_songs)
    
    with open("output.txt", "w") as output_file:
        output_file.write(formatted_matched_songs)
