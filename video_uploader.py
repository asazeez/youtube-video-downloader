from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

def google_drive():
    g_login = GoogleAuth()
    g_login.LocalWebserverAuth()
    drive = GoogleDrive(g_login)
    path = r"C:\Users\atiya\PycharmProjects\video_downloader"
    for file in os.listdir(path):
        if "mp4" in file:
            f = drive.CreateFile({'title': file})
            f.SetContentFile(os.path.join(path, file))
            f.Upload()
            print(file)