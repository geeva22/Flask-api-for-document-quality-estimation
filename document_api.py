import os
import cv2
from PIL import Image
import time
import numpy as np
import pickle
from flask import Flask
import pandas as pd
import jsonpickle

app = Flask(__name__)

@app.route('/')
def index():
    count = 1
    a = []
    #api endpoint of doucment data
    path = "https://github.com/geeva22/Flask-api-for-document-quality-estimation/Aadhar/" #C:\Users\Admin\Downloads\Work-idrbt\crops\Aadhar

    for file_name in os.listdir(path):
        if file_name.split(".")[-1].lower() in {"jpeg", "jpg", "png"}:
            img = cv2.imread(path + file_name)
            grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            lapla = cv2.Laplacian(grey, cv2.CV_64F).var()
            count += 1
            a.append(file_name)
            a.append(lapla)

    def Convert(a):
        it = iter(a)
        res_dct = dict(zip(it, it))
        return res_dct

    lst = a
    s = sorted(Convert(lst).items(), key=lambda x: x[1])
    m = s[-1][0]
    # print('Better quality image -',m)
    #end = time.perf_counter()
    # print('Execution time -',end-start)
    im = Image.open(path + m)
    out = np.array(im)
    lis = out.tolist()
    return jsonpickle.encode(lis)

if __name__ =="__main__":
    app.run(debug=True)
