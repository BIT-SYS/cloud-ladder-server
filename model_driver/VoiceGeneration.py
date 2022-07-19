# -*- coding = utf-8 -*-
# @Time : 2022/7/2 0:08
# @Author : kimi
# @File : t2a.py
# @Software : PyCharm
import pyttsx3

def use_pyttsx3(rate, volume, voice, words):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)

    # 设置新的语音音量，音量最小为 0，最大为 1
    engine.setProperty('volume', volume)

    voices = engine.getProperty('voices')
    # 设置当前语音声音为女性，当前声音不能读中文
    if (voice == "female"):
        engine.setProperty('voice', voices[1].id)
    else:
        engine.setProperty('voice', voices[0].id)
    print(rate, volume, voice, words)
    engine.save_to_file(words, 'out.mp3')
    engine.runAndWait()
    return "out.mp3"
