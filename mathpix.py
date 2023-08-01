from flask import Flask, request

app = Flask(__name__)
from PIL import Image
from pix2tex.cli import LatexOCR


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part in the request", 400

    file = request.files['file']

    if file.filename == '':
        return "No selected file", 400
    
    img = Image.open(file.stream)
    model = LatexOCR()
    result = model(img)

    return result, 200

if __name__ == '__main__':
    app.run(debug=True)
