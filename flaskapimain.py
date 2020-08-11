import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post_json():
    posteddata = request.data.decode('utf-8') # POSTされたデータを読み込む
    data = json.loads(posteddata) # POSTされたbytes形式のファイルをjsonファイルに変換する
    #humdata = humdata['humid'] # 地所型でkeyを指示して値を取り出す
    return str(data)

@app.route('/get', methods=['GET'])
def get_json():
    return 'This is get method!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


