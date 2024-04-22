import os
import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

URL = "https://www.billboard.com/charts/hot-100/"
CLIENTID = os.environ['CLIENTID']
SECRETCLIENT = os.environ['SECRET']
scope = "playlist-modify-private"
path = "token.txt"

sp_oath = SpotifyOAuth(CLIENTID,SECRETCLIENT, redirect_uri="https://example.com/", scope=scope, cache_path=path)
sp = spotipy.Spotify(sp_oath.get_access_token()['access_token'])
# print(sp_oath.get_access_token()['access_token'])


# user_id = sp.current_user()["id"]
# # print(user_id)
# urn = ['1WsHKAuN9vDthcmimdqqaY', '34I6QYP9yREZnvVZvDIo1']
# song = sp.playlist_add_items(playlist_id="58NTo8Qz7MmsnYgskyWTNL", items=urn, position=None)
# print(song)
# user = sp.user(username)
print(sp.search("track:Lovin On Me year 2024", limit=1, type='track', offset=0))


# time_travel = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")
# final_url = f"{URL}{time_travel}/"
# print(final_url)
# response = requests.get(url=final_url)
# soup = BeautifulSoup(response.text, 'html.parser')
# song_titles = [title.find(id="title-of-a-story").get_text().strip() for title in soup.find_all(class_="o-chart-results-list-row-container")]
