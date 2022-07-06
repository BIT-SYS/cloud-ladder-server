import io
import uuid
import os
sys.path.append("../models")
from SpeechRecognition import speech_recognition as sr

basedir = 'data/tmp'
if not os.path.exists(basedir):
    os.mkdir(basedir)

def inference(audio,lang):
    id = str(uuid.uuid1())
    dirname = basedir + "/" + id + "/"
    os.mkdir(dirname)
    audio.save(dirname + "demo_audio.wav")
    audio_file = 'demo_audio.wav'
    r = sr.Recognizer
    with sr.AudioFile(audio_file) as source:
        audio = r().record(source)
    return '文本内容：'+ r().recognize_sphinx(audio,language=lang)
