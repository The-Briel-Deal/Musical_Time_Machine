from time_music_scraper import MusicScrape
import requests
import os
import json

scrapa = MusicScrape()
list_of_songs = scrapa.return_noods()

# ------ Create Playlist ------ #
key = os.environ.get('spotify_key')
header = {'Authorization': f'Bearer {key}'}
body = {
    "name": "1985",
    "description": "Top 100 songs from 1985",
    "public": True
}

created_playlist = requests.post(url='https://api.spotify.com/v1/users/spartaofdoom/playlists',
                                 headers=header,
                                 json=body)
playlist_dict = json.loads(created_playlist.text)
playlist_id = playlist_dict['id']
# ------ Query for songs UID ------ #
uid_list = []
for song in list_of_songs:
    song_req = requests.get(url='https://api.spotify.com/v1/search',
                        headers=header,
                        params={
                            'q': song,
                            'type': 'track'
                        })

    song_dict = json.loads(song_req.text)
    song_uri = song_dict['tracks']['items'][0]['uri']
    uid_list.append(song_uri)
print(uid_list)
bleh = requests.post(url=f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
                     headers={'Authorization': f'Bearer {key}'},
                     json={"uris": uid_list}
                     )
print(bleh)
