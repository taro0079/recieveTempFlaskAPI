import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session
import json
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post_json():
    posteddata = request.data.decode('utf-8') # POSTされたデータを読み込む
    data = json.loads(posteddata) # POSTされたbytes形式のファイルをjsonファイルに変換する
    date = data['date']
    temp = data['temp']

    with open(fn, 'a') as f:
        writer = csv.writer(f)
        writedata = [date, temp]
        writer.writerow(writedata)

    return str(data)

# GET REQUESTの場合
@app.route('/get', methods=['GET'])
def get_json():
    datelst = []
    templst = []
    with open(fn, 'r') as f:
        for row in csv.DictReader(f):
            templst.append(float(row['temp']))
            datelst.append(float(row['date']))

    rejsondata = {'date' : datelst, 'temp' : templst}
    return json.dumps(rejsondata).encode('utf-8')

    #return 'This is get method!'


if __name__ == '__main__':

    # 記録用csvファイルを作成する
    fn = './data.csv' # ファイル名の設定
    # ファイルが存在しない場合の処理 -> csvファイルを作る
    if os.path.exists(fn) == False:
        with open(fn, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['date', 'temp']) # csv headers
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


