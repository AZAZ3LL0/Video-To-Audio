import telebot
from telebot import types
from pytube import YouTube
import os
from moviepy.editor import *


token = input('PUT UR BOT TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/download 'LINK'")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    yt = YouTube(message.text)

    vidos = "".join(char for char in yt.title if char.isalnum())
    print(vidos)
    try:
        yt.streams.filter(file_extension='mp4')[0].download(filename=vidos + ".mp4")

    except KeyError:
        bot.send_message(message.chat.id, 'this video cant be converted((((sorry')
        print('this video cant be converted')
    finally:
        try:
            video = VideoFileClip(vidos + ".mp4")
            video.audio.write_audiofile(vidos + ".mp3")

            audio = open(vidos + ".mp3", 'rb')
            # yield bot.send_audio(message.chat.id, audio)
            bot.send_audio(message.chat.id, audio)

            video.close()
            audio.close()
            os.remove(vidos + ".mp4")
            os.remove(vidos + ".mp3")
        except OSError:
            pass


@bot.message_handler(commands=['download'])
def sent_group_audio(message):
    yt = YouTube(message.text.split(' ')[-1])
    vidos = "".join(char for char in yt.title if char.isalnum())
    print(vidos)
    try:
        yt.streams.filter(file_extension='mp4')[0].download(filename=vidos + ".mp4")

    except KeyError:
        bot.send_message(message.chat.id, 'this video cant be converted((((sorry')
        print('this video cant be converted')
    finally:
        try:
            video = VideoFileClip(vidos + ".mp4")
            video.audio.write_audiofile(vidos + ".mp3")

            audio = open(vidos + ".mp3", 'rb')
            # yield bot.send_audio(message.chat.id, audio)
            bot.send_audio(message.chat.id, audio)

            video.close()
            audio.close()
            os.remove(vidos + ".mp4")
            os.remove(vidos + ".mp3")
        except OSError:
            pass


bot.infinity_polling(interval=0, timeout=5 * 60)