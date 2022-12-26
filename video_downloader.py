from pytube import YouTube
import sys
if len(sys.argv)>1:
    url = sys.argv[1]

else:
    sys.exit('enter video url')

yt = YouTube(url)
yt= yt.streams.filter(progressive=True).order_by("resolution").last()
try:
    yt.download()
except:
    print ('Error')

print ('successful download')




