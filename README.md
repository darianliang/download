# DOWNLOAD

A clean desktop app that downloads videos from services
such as YouTube, Twitter, and Instagram as mp3 or mp4 
files using a visual interface built using Python, HTML, 
and CSS. Only for MacOS currently

### How to use:
- install dependencies via pip install -r requirements.txt
- run the app via python app.py
- install ffmpeg via brew install ffmpeg
- install pillow via pip install pillow
- build the .app via
    pyinstaller --windowed --onefile \
    --add-data "gui.html:." \
    --add-data "style.css:." \
    --add-data "myfont.otf:." \
    --icon download.icns \
    --name "Download" \
    app.py
- app will save in repository dist folder
- drag to applications folder if desired
- open app, paste YouTube url
- choose mp3 or mp4
- click begin
- file will save in desktop folder
- close app and open again to run the app again