import speech_recognition as sr
import io
import base64

def inference(b64_data,lang):
    wav_bytes = base64.b64decode(b64_data)
    id = str(uuid.uuid1())
    dirname = basedir + "/" + id + "/"
    os.mkdir(dirname)
    f = open(dirname + "demo_audio.wav", 'wb')
    f.write(wav_bytes)
    f.close()
    audio_file = 'demo_audio.wav'
    r = sr.Recognizer
    with sr.AudioFile(audio_file) as source:
        audio = r().record(source)
    return '文本内容：'+ r().recognize_sphinx(audio,language=lang)