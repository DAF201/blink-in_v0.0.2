from src.page_loader import style_sheet_loader, script_loader, favicon
from src.pages import login_page, home_page, music_playing, video_playing, blink_in
from src.shell import shell

# config file for page directing

direct = [
    (r'/', home_page),
    (r'/favico', favicon),
    (r'/scripts(.*)', script_loader),
    (r'/css(.*)', style_sheet_loader),
    (r'/login', login_page),
    (r'/shell(.*)', shell),
    (r'/music(.*)', music_playing),
    (r'/video(.*)', video_playing),
    (r'/APIs/blink_in', blink_in),
]
