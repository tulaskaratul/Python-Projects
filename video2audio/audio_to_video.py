import os
from pytube import YouTube
import pytube


def main():
    
    video_url= str(input("Enter youtube URL : "))

    print ("Download started")
    if os.name == 'nt':
        path = os.getcwd() + '\\'
    else:
        path = os.getcwd() + '/'

    name = pytube.extract.video_id(video_url)

    #print(name)

    #YouTube(video_url).streams.filter(file_extension="mp3").first().download()
    yt = YouTube(video_url)

    yt.streams.filter(only_audio=True).first().download(filename=name + '.mp3')
#    name = yt.title
    print("Download completed")
    location = path + name + '.mp3'

    # renmame_to_mp3 =  path + name + '.mp3'

    print("Download location = ",location)

    # # print("rename to mp3 = ",renmame_to_mp3)

    # if os.name == 'nt':
    
    #     os.system('ren {0} {1}'.format(location, renmame_to_mp3))
    # else:
        
    #     os.system('mv {0} {1}'.format(location, renmame_to_mp3))


if __name__ == '__main__':

    main()
