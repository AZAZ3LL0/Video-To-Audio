from pytube import YouTube
import os
from moviepy.editor import *
import argparse
from tools import titles


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=False)
parser.add_argument("-s", "--stream", required=False)
parser.add_argument("-f", "--fullcontrol", required=False)
args = parser.parse_args()

print(titles.intro2)


def main():
    if args.path is not None:
        path = args.path + "/"
    else:
        path = ""
    while True:
        request = input("YT link:\t")
        if request == "exit" or request == KeyboardInterrupt:
            break

        yt = YouTube(request)
        normal_name = "".join(char for char in yt.title if char.isalnum())
        print(normal_name)

        try:
            streams = yt.streams.filter(file_extension='mp4')
            if args.fullcontrol is not None:
                [print(i) for i in streams]
                streams[int(input("\nВведите индекс стрима:\t"))].download(filename=normal_name + ".mp4")
            else:
                streams[0].download(filename=normal_name + ".mp4")

        except KeyError:
            print('this video cant be converted')
        finally:
            try:
                video = VideoFileClip(normal_name + ".mp4")
                video.audio.write_audiofile(path + normal_name + ".mp3")
                video.close()
                os.remove(normal_name + ".mp4")
            except OSError:
                pass

        if args.stream is None:
            break


if __name__ == "__main__":
    main()
