from random import random
from PIL import Image

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello, i'm Chloe!"


@app.route("/upload", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)

    return jsonify({'msg': 'success', 'possibility': ['{:.2f}'.format(random())]})


if __name__ == '__main__':
    app.run()
# pip freeze > requirements.txt
