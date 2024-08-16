from flask import Flask, render_template, request, jsonify
from PIL import Image
import io
import base64
app = Flask(__name__, template_folder='templates', static_folder='static')

imgFolder = r"C:\Users\admin\OneDrive\Desktop\Codeblaze\Signs\\"
signDictionary = {
    'A': 'A.jpg',
    'B': 'B.jpg',
    'C': 'C.jpg',
    'D': 'D.jpg',
    'E': 'E.jpg',
    'F': 'F.jpg',
    'G': 'G.jpg',
    'H': 'H.jpg',
    'I': 'I.jpg',
    'J': 'J.jpg',
    'K': 'K.jpg',
    'L': 'L.jpg',
    'M': 'M.jpg',
    'N': 'N.jpg',
    'O': 'O.jpg',
    'P': 'P.jpg',
    'Q': 'Q.jpg',
    'R': 'R.jpg',
    'S': 'S.jpg',
    'T': 'T.jpg',
    'U': 'U.jpg',
    'V': 'V.jpg',
    'W': 'W.jpg',
    'X': 'X.jpg',
    'Y': 'Y.jpg',
    'Z': 'Z.jpg',
}

def textToSign(text):
    signImages = []

    for letter in text.upper():
        if letter in signDictionary:
            imgPath = imgFolder + signDictionary[letter]
            try:
                img = Image.open(imgPath)
                signImages.append(img)
            except FileNotFoundError:
                print(f"Image not found for letter: {letter}")

    return signImages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST', 'GET'])
def translate():
    if request.method == 'POST':
        text_to_translate = request.form.get('text-to-be-translated')
        translated_images = textToSign(text_to_translate)

        # Convert images to base64 for sending to the frontend
        image_data_list = []
        for img in translated_images:
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            image_data_list.append(img_str)

        return jsonify(images=image_data_list)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)