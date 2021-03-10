# -*- coding: utf-8 -*-

import os
from bottle import route, run


@route("/")
def hello_world():
    return "" # ここで返す内容は何でもよい

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

#これはherokuで動かしておくために必要なダミーWEBアプリです。
#軽量フレームワークのbottleを使用しています。
# https://qiita.com/enomotok/items/41275dd904c8aa774e72