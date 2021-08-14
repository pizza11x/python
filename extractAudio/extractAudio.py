import pytube
import os


def main():
    #Get url from User
    video_url = input('Enter Youtube video URL: ')
    #get current Path
    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    #Get id video
    name = pytube.extract.video_id(video_url)
    #Download only_audio from youtube
    pytube.YouTube(video_url).streams.filter(only_audio=True).first().download(filename=name)
    location = path + name
    renametomp3 = path + name + '.mp3'

    #Give extension to file
    if os.name == 'nt':
        os.system('ren {0} {1}'.format(location, renametomp3))
    else:
        os.system('mv {0} {1}'.format(location, renametomp3))


if __name__ == '__main__':
    main()
