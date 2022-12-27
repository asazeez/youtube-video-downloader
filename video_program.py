import os

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

def video_delete():
    path = r"C:\Users\atiya\PycharmProjects\video_downloader"
    for file in os.listdir(path):
        if "mp4" in file:
            ans = input("Delete" + file + "? ")
            if ans == 'yes':
                try:
                    os.remove(file)
                except:
                    print ('unable to delete file')

if len(sys.argv)>1:
   print (sys.argv)
   for x in sys.argv:
      if "https" in x:
         downloader(x)
else:
    sys.exit('enter video url')

video_uploader.google_drive()
video_delete()
