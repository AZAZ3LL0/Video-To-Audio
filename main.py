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
    vidos = yt.title.replace('.', '')
    print(vidos)
    yt.streams.filter(file_extension='mp4')[0].download()
    video = VideoFileClip(vidos + ".mp4")
    video.audio.write_audiofile(vidos + ".mp3")

    audio = open(vidos + ".mp3", 'rb')
    # yield bot.send_audio(message.chat.id, audio)
    bot.send_audio(message.chat.id, audio)

    video.close()
    audio.close()
    os.remove(vidos + ".mp4")
    os.remove(vidos + ".mp3")
    #except BaseException:
    #    bot.reply_to(message, "Еблан? Ссылку гони сучара")

@bot.message_handler(commands=['download'])
def sent_group_audio(message):
    yt = YouTube(message.text.split(' ')[-1])
    vidos = yt.title.replace('.', '')
    print(vidos)
    yt.streams.filter(file_extension='mp4')[0].download()
    video = VideoFileClip(vidos + ".mp4")
    video.audio.write_audiofile(vidos + ".mp3")

    audio = open(vidos + ".mp3", 'rb')
    # yield bot.send_audio(message.chat.id, audio)
    bot.send_audio(message.chat.id, audio)

    video.close()
    audio.close()
    os.remove(vidos + ".mp4")
    os.remove(vidos + ".mp3")

bot.infinity_polling(interval=0, timeout=5 * 60)
