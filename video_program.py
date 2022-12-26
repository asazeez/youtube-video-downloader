from pytube import YouTube
import sys
import video_uploader


def downloader (url):
    yt = YouTube(url)
    yt= yt.streams.filter(progressive=True).order_by("resolution").last()
    try:
        yt.download()
    except:
        print ('Error')
    print ('successful download')


if len(sys.argv)>1:
    print (sys.argv)
    for x in sys.argv:
        if "https" in x:
            downloader(x)
else:
    sys.exit('enter video url')

video_uploader.google_drive()