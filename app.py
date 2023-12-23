import numpy as np
import pandas as pd  
from flask import Flask, render_template,jsonify,request

import config
from utilities import CropSystem

app = Flask(__name__)

@app.route("/")
def home_app():
    return render_template('index.html')

@app.route("/prediction",methods=['POST','GET'])
def predict_crop():
    if request.method=='POST':
        data = request.form
        N = float(data['N'])
        P = float(data['P'])
        K = float(data['K'])
        temperature = float(data['temperature'])
        humidity = float(data['humidity'])
        ph = float(data['ph'])
        rainfall = float(data['rainfall'])

        cropsystem = CropSystem(N,P,K,temperature,humidity,ph,rainfall)
        crop = cropsystem.recommended_crop()

    return render_template('index.html', result=crop)

if __name__=="__main__":
    app.run(debug=True,port=config.PORT, host=config.HOST)


# AgroGuideHub

        





