from flask import Flask, request
import model_driver.ImageCaptioning as im2text


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


if __name__ == "__main__":
    # 启动服务器，运行在5000端口上
    app.run(debug=True)
