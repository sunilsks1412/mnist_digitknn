import pandas as pd
from flask import Flask, render_template, request
import pickle
import numpy as np
import base64
from PIL import Image
import PIL


app = Flask(__name__)
knn = pickle.load(open('knn_pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    img = request.form.get('image').replace('data:image/png;base64,','')
    img = img.encode()
    print(type(img))

    with open("image.png","wb") as fh:
        fh.write(base64.decodebytes(img))
    
    im = Image.open('image.png').convert('RGBA')
    #white
    bg = Image.new('RGBA', im.size, (255,255,255))

    alpha = Image.alpha_composite(bg,im)
    # alpha = im
    alpha = alpha.convert('L')  #bw
    alpha = alpha.resize((28,28))


    image_np = np.array(alpha).reshape(784,)

    lst = []
    for i in image_np:
        if i==255:
            lst.append(0)
        else:
            lst.append(i)
    

    print(lst)
    # print(image_np)
    print(image_np.shape)


    prediction = knn.predict([image_np])
    return str(prediction)

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port = 9696)