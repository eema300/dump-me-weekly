import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'your client id here'
CLIENT_SECRET = 'your client secret here'
REDIRECT_URI = 'http://localhost:8888/'
SCOPES = 'playlist-read-private playlist-modify-private playlist-modify-public'
CACHE = 'path/to/.cache'

# authorize user access (use authorization code flow since it's just a script)
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope=SCOPES,
                        cache_path=CACHE)


sp = spotipy.Spotify(auth_manager=sp_oauth)
user_id = sp.me()['id']

# locate discover weekly and dump me weekly playlists in user library (must use pagination)
playlists_page = sp.current_user_playlists(limit=50)
user_playlists = playlists_page['items']
discover_weekly_id = None
dump_me_weekly_id = None

while playlists_page['next']:
    playlists_page = sp.next(playlists_page)
    user_playlists.extend(playlists_page['items'])

for playlist in user_playlists:
    if 'Discover Weekly' == playlist['name']:
        discover_weekly_id = playlist['id']
    if 'Dump Me Weekly' == playlist['name']:
        dump_me_weekly_id = playlist['id']

# create dump playlist if it does not exist
if dump_me_weekly_id is None:
    dump_me_weekly = sp.user_playlist_create(user=user_id, 
                                                name='Dump Me Weekly', 
                                                public=False, 
                                                description='Saves your Discover Weekly so you never miss another great song.')
    dump_me_weekly_id = dump_me_weekly['id']
    print('playlist created')

# get discover weekly items (use pagination)
discover_weekly_tracks = sp.playlist_tracks(playlist_id=discover_weekly_id, limit=100)
discover_weekly_items = discover_weekly_tracks['items']

while discover_weekly_tracks['next']:
    discover_weekly_tracks = sp.next(discover_weekly_tracks)
    discover_weekly_items.extend(discover_weekly_tracks['items'])

# get uris of those tracks
discover_weekly_items_uris = [item['track']['uri'] for item in discover_weekly_items]

# copy songs over from discover to dump
sp.playlist_add_items(playlist_id=dump_me_weekly_id, items=discover_weekly_items_uris)