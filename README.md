# Wefunkradio Show Downloader
This python script is used to download and encode shows from Wefunkradio.com
The original mp3 file downloaded is typically about 200mb so I'm using FFMPEG (which you need to install) to transcode the mp3 down to a VBR -V8 which I found gives the smallest file size (around 100mb per show) without noticably ruining the audio quality. 

# What You Need
- [Python 3](https://www.python.org/downloads/)
- [FFMPEG](https://www.ffmpeg.org/download.html) (optional)
- The requests library 
Install requests library with
```
pip install requests
```

## Usage
Just run the script with the show number you'd like to download as an argument. 

```
wefunkdlencode.py SHOWNUMBER
```
or without encoding step
```
wefunkdl.py SHOWNUMBER
```
## Optional .BAT file
If you want to download and encode lots of shows, just run the .BAT file. It will ask you for a minimum and maximum show number and it will download and encode all of those shows. It will also check to see if any of those files (converted or original) already exist and it will skip the download step, encode step or both steps and move on to the next show. 

There's two .BAT files to use depending on whether you want to encode or not. 