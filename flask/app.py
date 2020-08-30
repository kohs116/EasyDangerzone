from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#파일 업로드 처리
@app.route('/fileUpload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      #저장할 경로 + 파일명
      filename = f.filename
      path = '/tmp/'
      f.save(path + secure_filename(filename))
      uploadpath = " " + path + filename + " "

      subprocess.call(["/usr/bin/dangerzone-container" " documenttopixels --document-filename" + uploadpath + "--pixel-dir /tmp/dangerzone-pixel --container-name flmcode/dangerzone"], shell=True)
      subprocess.call(["/usr/bin/dangerzone-container" " pixelstopdf --pixel-dir /tmp/dangerzone-pixel --safe-dir /tmp/dangerzone-safe --container-name flmcode/dangerzone --ocr 0 --ocr-lang eng"], shell=True)

      os.rename("/tmp/dangerzone-safe/safe-output-compressed.pdf", "/tmp/dangerzone-safe/" + filename + "_" + "safe-output.pdf")

      return send_file("/tmp/dangerzone-safe/" + filename + "_" + "safe-output.pdf", mimetype='application/pdf')


if __name__ == '__main__':
    #서버 실행
   app.run(host='0.0.0.0',port=5000,debug = True)
