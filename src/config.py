import os
import json

# loging page username and password
credentials = {'admin': 'admin'}

# static files folder
STATIC_HTML = os.getcwd()+'\\static_htmls\\'
STATIC_FILE = os.getcwd()+'\\static_files\\'
STATIC_JS = os.getcwd()+'\\static_js\\'
STATIC_CSS = os.getcwd()+'\\static_css\\'
MUSIC_PLAYLIST = os.getcwd()+'\\music_playlist\\'
VIDEO_PLAYLIST = os.getcwd()+'\\video_playlist\\'
FAVICON = 'favicon.ico'
HOME_PAGE = 'home.html'
LOGIN_PAGE = 'login.html'

# cookie database
COOKIE_DATA_BASE = os.getcwd()+'\\db\\cookie.json'
with open(COOKIE_DATA_BASE)as cookie_db:
    cookie_data = json.load(cookie_db)

# port
PORT = 80

# storage
GITHUB_TOKEN = ''
GITHUB_REPO_ADDRESS = ''
