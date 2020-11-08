import imghdr
import os
from soundReco import printmew
from random import random
os.environ['CUDA_VISIBLE_DEVICES'] = ''

from PIL import Image
from flask_cors import CORS, cross_origin
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory, Response, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


@app.errorhandler(413)
def too_large(e):
    return "File is too large", 413


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=['POST', 'OPTIONS'])
@cross_origin()
def upload_files():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    return jsonify({'msg': 'success', 'size': [img.width, img.height],'possibility': '{:.2f}'.format(random()*100)})



@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)
