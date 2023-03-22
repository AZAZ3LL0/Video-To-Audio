from pytube import YouTube
import os
from moviepy.editor import *
import argparse
from tools import titles


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--path", required=False)
parser.add_argument("-s", "--stream", required=False)
args = parser.parse_args()

print(titles.intro2)


def main():
    if args.path is not None:
        path = args.path
    else:
        path = ""
    while True:
        request = input("YT link:\t")
        if request == "exit" or request == KeyboardInterrupt:
            break

        yt = YouTube(request)

        print(yt.title)

        yt.streams.filter(file_extension='mp4')[0].download()
        video = VideoFileClip(yt.title + ".mp4")
        video.audio.write_audiofile(path + "/" + yt.title + ".mp3")

        video.close()
        os.remove(yt.title + ".mp4")

        if args.stream is None:
            break


if __name__ == "__main__":
    main()
