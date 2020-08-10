import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/post', methods=['POST'])
def post_json():
    return 'This is post'

@app.route('/get', methods=['GET'])
def get_json():
    return 'This is get method!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


