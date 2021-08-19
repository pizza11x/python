import pytube
from pytube import YouTube
from tkinter import *
import os

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("Youtube audio extract")

Label(root, text='Youtube audio extract', font='arial 20 bold').pack()
link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=70)
areaLink = Entry(root, width=50, textvariable=link).place(x=45, y=110)


def download():
    # Get url from User
    video_url = str(link.get())
    # get current Path
    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    # Get id video
    name = pytube.extract.video_id(video_url)
    # Download only_audio from youtube
    YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)

    if os.name == 'nt':
        location = path + name + '.mp4'
    else:
        location = path + name

    renametomp3 = path + name + '.mp3'

    # Give extension to file
    if os.name == 'nt':
        os.system('ren {0} {1}'.format(location, renametomp3))
    else:
        os.system('mv {0} {1}'.format(location, renametomp3))

    Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)


Button(root, text='Download', font='arial 15 bold', bg='pale violet red', padx=2, command=download).place(x=190, y=150)

root.mainloop()
