from flask import Flask, request
import model_driver.ImageCaptioning as im2text
import model_driver.SpeechRecognition as sr
import model_driver.TextGeneration as text2img
import model_driver.VoiceGeneration as text2audio

app = Flask(__name__)


# 示例接口，用于测试服务器是否正常工作
@app.route('/test')
def get_test_msg():
    return "Hello World"


# 图片转文字，使用post请求上传图片，图片数据保存在image字段中
@app.route('/inference', methods=['POST'])
def get_caption_text():
    img = request.files.get('image')
    # 调用分装好的推理函数
    return im2text.inference(img)

# 语音转文字，使用post请求上传wav音频，音频数据保存在audio_file字段中，识别的语言类型保存在lang中
@app.route('/speech_recognition', methods=['POST'])
def get_speech():
    audio_file = request.files.get('audio')
    lang =  request.form.get('lang')
    print(lang)
    if (lang != 'en-US') and (lang != 'zh-CN'):
        return 'warning:不支持的语言识别'
    return sr.inference(audio_file,lang)

# 从POST请求中读取字符串，调用Dall-E Mini模型进行推理，将推理结果封装在file中返回
@app.route('/text2image', methods=['POST'])
def get_generated_image():
    text = request.form.get('text')
    return text2img.inference(text)

@app.route('/voice_conversion', methods=['POST'])
def get_audio():
    audio_file = request.files.get('audio')
    type = request.form.get('aParam')
    if (type != 'high') and (type != 'low'):
        return 'error:请输入正确的变音指令'
    return vc.inference(audio_file,type)

@app.route('/t2a', methods=['GET', 'POST'])
def t2a():
    if request.method == 'GET':
        rate = request.args.get('rate')
        volume = request.args.get('volume')
        voice = request.args.get('voice')
        words = request.args.get('words')
        return send_file(main.use_pyttsx3(rate, volume, voice, words), as_attachment=True)
    if request.method == 'POST':
        rate = request.form.get('rate')
        volume = request.form.get('volume')
        voice = request.form.get('voice')
        words = request.form.get('words')   
        return send_file(main.use_pyttsx3(rate, volume, voice, words), as_attachment=True)


if __name__ == "__main__":
    # 启动服务器，运行在5000端口上
    app.run(host='0.0.0.0',port=5000,debug=True)
