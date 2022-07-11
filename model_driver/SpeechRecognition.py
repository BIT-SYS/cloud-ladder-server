import speech_recognition as sr
import io
import uuid
import os

root = 'data/'
if not os.path.exists(root):
    os.mkdir(root)
subdirectory = root + 'tmp/'
if not os.path.exists(subdirectory):
    os.mkdir(subdirectory)
def inference(audio,lang):
    id = str(uuid.uuid1())
    dirname = subdirectory + "/" + id + "/"
    os.mkdir(dirname)
    audio.save(dirname + "demo_audio.wav")
    audio_file = dirname + 'demo_audio.wav'
    r = sr.Recognizer
    with sr.AudioFile(audio_file) as source:
        audio = r().record(source)
    return '文本内容：'+ r().recognize_sphinx(audio,language=lang)
