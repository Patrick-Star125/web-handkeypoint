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
    raw_imgpath = "static/raw.png"
    process_imgpath = "static/processed.png"
    if request.method == 'POST':
        if os.path.exists(process_imgpath):
            os.system("rm -r {}".format(process_imgpath))
        if os.path.exists(raw_imgpath):
            os.system("rm -r {}".format(raw_imgpath))
        f = request.files['file']
        upload_path = os.path.join('./static/raw.png')  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)

        keypoint_extraction(raw_imgpath, process_imgpath)
        img_url = url_for('static', filename='processed.png')
        data = {'img_url': img_url}
        print(data)
        data = json.dumps(data)
        return data


if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5500)
