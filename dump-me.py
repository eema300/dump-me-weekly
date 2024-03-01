# this is a practice python file for backend
import spotipy
from spotipy import SpotifyOAuth


# function definitions

def get_playlist_id(user_playlists, name):
    playlist_id = None
    for playlist in user_playlists['items']:
        if name == playlist['name']:
            playlist_id = playlist['id']
            break
    return playlist_id


def get_tracklist(track_info):
    tracklist = []
    for track in track_info['items']:
        tracklist.append(track['uri'])
    return tracklist


# authentication constants

SCOPES = ['playlist-modify-private", "playlist-read-private']
CLIENT_ID = 'removed'
CLIENT_SECRET = 'removed'
REDIRECT_URI = 'http://localhost:8080'
PORT_NUM = 8080

# create oauth and spotify objects

oauth = SpotifyOAuth(CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, scope=SCOPES)
sp = spotipy.Spotify(auth_manager=oauth)

# get current user details

user_info = sp.current_user()
user_id = user_info['id']

# access endpoint: list of user's playlists --> find and save dump me and discover weekly playlist ids

playlists = sp.current_user_playlists()
dump_me_weekly_id = get_playlist_id(playlists, 'Dump Me Weekly')
discover_weekly_id = get_playlist_id(playlists, 'Discovery Weekly')

# create dump me weekly playlist if it does not exist

if not dump_me_weekly_id:
    sp.user_playlist_create(user_id, 'Dump Me Weekly',
                            description='saving your discovery weekly so you never miss another great song')

# get length of dump me weekly to find end position

playlists.clear()
playlists = sp.current_user_playlists()
dump_me_weekly_id = get_playlist_id(playlists, 'Dump Me Weekly')
dump_me_weekly_playlist_info = sp.playlist(dump_me_weekly_id)
num_tracks = dump_me_weekly_playlist_info['tracks']['total']

# access endpoint: get list of track URLs from Discover Weekly playlist

discover_weekly_tracks_info = sp.playlist_items(discover_weekly_id, limit=num_tracks)
discover_weekly_tracks = get_tracklist(discover_weekly_tracks_info)

# add tracks to dump me weekly

sp.playlist_add_items(dump_me_weekly_id, discover_weekly_tracks, num_tracks)
