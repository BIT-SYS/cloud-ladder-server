from flask import Flask, request
import model_driver.ImageCaptioning as im2text


app = Flask(__name__)


@app.route('/test')
def get_test_msg():
    return "Hello World"


@app.route('/im2text', methods=['POST'])
def get_caption_text():
    img = request.files.get('image')
    return im2text.inference(img)


if __name__ == "__main__":
    app.run(debug=True)
