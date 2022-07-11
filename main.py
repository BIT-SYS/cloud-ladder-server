from flask import Flask, request
import model_driver.ImageCaptioning as im2text
import model_driver.SpeechRecognition as sr


app = Flask(__name__)


# 示例接口，用于测试服务器是否正常工作
@app.route('/test')
def get_test_msg():
    return "Hello World"


# 图片转文字，使用post请求上传图片，图片数据保存在image字段中
@app.route('/im2text', methods=['POST'])
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

if __name__ == "__main__":
    # 启动服务器，运行在5000端口上
    app.run(debug=True,host='0.0.0.0',port=5000)
