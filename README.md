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
