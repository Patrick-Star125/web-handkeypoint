from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from imgprocess import keypoint_extraction
import os, json

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/index.css', methods=['POST', 'GET'])
def css():
    return render_template('index.css')


@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        img_name = f.filename
        raw_imgpath = "static\\raw-{}.png".format(img_name)
        process_imgpath = "static\\processed-{}.png".format(img_name)
        f.save(raw_imgpath)  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径

        img_exist = keypoint_extraction(raw_imgpath, process_imgpath)
        img_url = url_for('static', filename='processed-{}.png'.format(img_name))
        data = {'img_url': img_url, 'img_exist': img_exist}
        print(data)
        data = json.dumps(data)
        return data


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5500)
