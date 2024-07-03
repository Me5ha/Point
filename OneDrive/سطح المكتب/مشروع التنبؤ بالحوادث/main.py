from flask import Flask, render_template, request
import pandas as pd
# from sklearn.externals import joblib
# import sklearn.external as extjoblib
import joblib
import numpy as np
import urllib.request
import urllib.parse

app = Flask(__name__)
model = joblib.load('model.sav')


def cal(ip):
    input = dict(ip)
    Did_Police_Officer_Attend = input['Did_Police_Officer_Attend'][0]
    age_of_driver = input['age_of_driver'][0]
    vehicle_type = input['vehicle_type'][0]
    age_of_vehicle = input['age_of_vehicle'][0]
    engine_cc = input['engine_cc'][0]
    day = input['day'][0]
    weather = input['weather'][0]
    light = input['light'][0]
    roadsc = input['roadsc'][0]
    gender = input['gender'][0]
    speedl = input['speedl'][0]

    data = np.array([Did_Police_Officer_Attend, age_of_driver, vehicle_type, age_of_vehicle, engine_cc, day, weather, roadsc, light, gender, speedl])

    print("logging",data)
    data = data.astype(float)
    data = data.reshape(1, -1)

    x = np.array([1, 3.73, 3, 0.69, 125, 4, 1, 1, 1, 1, 30]).reshape(1, -1)

    try: result = model.predict(data)
    except Exception as e: result = str(e)

    return str(result[0])


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def get():
    return cal(request.form)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)
