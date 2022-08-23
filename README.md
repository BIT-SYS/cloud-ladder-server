# cloud-ladder 服务端

使用flask作为服务端，从CL向服务端发出HTTP请求，将模型输出值以HTTP响应的方法返回.
- main.py 中进行模型初始化和调用
- 模型调用时需要设置的初始化参数和调用的过程封装在model_driver包中

### 安装
#### Image Captioning 任务
[配置文档](https://www.wolai.com/bkaoVrJGpQiiGhmQWnKQWD)

#### 图片生成任务
```bash
pip install min-dalle
```
第一次启动时将会自动下载模型.

***
#### Speech Recognition 任务
__requirement：__  
pocketsphinx  
speech_recognition（该包应放在models/SpeechRecognition下）  
__语音模型：__  
1. 保存在models/SpeechRecognition/speech_recognition/pocketsphinx-data下，目前已经有英语(en-US)和普通话(zh-CN)两个模型。  
2. 如需要更多预训练模型，可前往：https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/下载  
3. 下载好的模型或者自行训练的模型请参考第一条中的模型进行存放和命名，自行训练模型可以参考https://blog.csdn.net/qiaocuiyu/article/details/52093803
4. 如果增加了模型，请在model_driver/SpeechRecognition.py中进行对应的修改以增加支持的语言。
#### Voice Conversion 任务
__requirement：__  
librosa  
__语音模型：__  
1. 目前只支持通过改变语调进行变声。
2. 可以尝试通过CycleGAN-VC2或pytorch-StarGAN-VC模型增加针对特定人物的变声模型。
# cloud-ladder server

this repo uses flask as WebServer backend framework, the cloud-ladder clients use HTTP requests to invoke machine learning APIs. The computed results will be returned as HTTP response.
- all the API calls should be handled in `main.py`
- the necessary (but long) codes to initialize ML models should be placed in the `model_driver` directory

### Installation
to setup your local cloud-ladder server, you should clone this repository and download the checkpoints & setup all the models.

#### Image Captioning
to install the image captioning model, please refer to this page [doc](https://www.wolai.com/bkaoVrJGpQiiGhmQWnKQWD).

#### Text to Image
``` bash
pip install min-dalle
```
the model checkpoints as well as other necessary files will be downloaded during the first launch

***
> References
- https://github.com/kuprel/min-dalle
#### Speech Recognition
__requirement：__  
pocketsphinx  
speech_ Recognition (this package should be placed under models/speechrecognition)  
__model：__
1. Save in models/speechrecognition/speech_recognition/pocketsphinx-data, there are two models: English (EN US) and Mandarin (zh CN).
2.  If you need more pre training models, you can go to: https://sourceforge.net/projects/cmusphinx/files/Acoustic%20and%20Language%20Models/
3. For downloaded models or self-trained models, please refer to the model in 1 for storage and naming, and the methods of self-trained models can be referred to https://blog.csdn.net/qiaocuiyu/article/details/52093803
4.  If a model is added, please enter it in the model_driver/SpeechRecognition.py to add supported languages.
#### Voice Conversion
__requirement：__  
librosa  
__model：__  
1. Currently, it only supports voice change by changing intonation.
2. You can try to add a voice change model for specific characters through cyclegan-vc2 or pytorch stargan VC model.
