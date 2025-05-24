# DOWNLOAD

A clean desktop app that downloads YouTube videos as mp3 
or mp4 files using a visual interface built using Python,
HTML, and CSS. 

### How to use:
- install dependencies via pip install -r requirements.txt
- run the app via python app.py
- install ffmpeg via brew install ffmpeg
- build the .app via
    pyinstaller --windowed --onefile \
    --add-data "gui.html:." \
    --add-data "style.css:." \
    --add-data "myfont.otf:." \
    --icon download.icns \
    --name "Download" \
    app.py

