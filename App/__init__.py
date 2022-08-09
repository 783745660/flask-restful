from flask import Flask
from App.exts import init_exts
from App.urls import *

def create_app():
    app = Flask(__name__)
    # 初始化插件
    init_exts(app)

    return app