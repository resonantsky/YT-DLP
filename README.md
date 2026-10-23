# YT-DLP
## Simple python youtube video puller

Need a simple free-for-ever, no strings attached Youtube and other streaming services video downloader? 

Look no further. 

A simple implementation of the python-based YT-DLP library.

### Installation

Needs a python venv, requirements.txt included.
```shell
CD YT-DLP
python -m venv venv
./venv/Scripts/Activate.ps1   # or ./venv/Scripts/activate.bat for CMD
pip install -r requirements.txt
```
#### yt-dlp.py

This is the regular Youtube video puller  
`python yt-dlp.py http://www.youtube.com/video_url`

#### yt-dlp-frag.py

This is the puller for various other streaming sites that use video fragmentation to save space server-side.  
`python yt-dlp-frag.py http://www.video-site.com/video_url`

