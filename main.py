import telebot
from pytube import YouTube
import os
from moviepy.editor import *


token = input()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Put youtube link")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    yt = YouTube(message.text)
    print(yt.title)
    yt.streams.filter(file_extension='mp4')[0].download()
    video = VideoFileClip(yt.title + ".mp4")
    video.audio.write_audiofile(yt.title + ".mp3")

    audio = open(yt.title + ".mp3", 'rb')
    # yield bot.send_audio(message.chat.id, audio)
    bot.send_audio(message.chat.id, audio)

    video.close()
    audio.close()
    os.remove(yt.title + ".mp4")
    os.remove(yt.title + ".mp3")
    #except BaseException:
    #    bot.reply_to(message, "Еблан? Ссылку гони сучара")


bot.infinity_polling(interval=0, timeout=5 * 60)
