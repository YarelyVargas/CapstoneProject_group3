from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os
import pickle
from modelHelper import ModelHelper
#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
modelHelper = ModelHelper()

# from modelHelper import ModelHelper
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")

@app.route("/aboutus")
def aboutus():
    # Return template and data
    return render_template("aboutus.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/datatable")
def datatable():
    # Return template and data
    return render_template("datatable.html")
@app.route("/sources")
def sources():
    # Return template and data
    return render_template("sources.html")

@app.route("/MLcreation")
def MLcreation():
    # Return template and data
    return render_template("MLcreation.html")

@app.route("/prediction")
def prediction():
    # Return template and data
    return render_template("prediction.html")
@app.route("/mypred")
def pred():
    # Return template and data
    return render_template("mypred.html")


# POST REQUEST LISTENER
@app.route("/makePredictions", methods=["POST"])
def makePrediction():
    content = request.json["data"]
    print(content)
    Scaler = pickle.load(open('scaler.sav', 'rb'))
    new = pd.DataFrame([content])
    cols7= ['MentalHealth', 'BMI', 'PhysicalHealth']
    new[cols7] = Scaler.transform(new[cols7])
    # parse
    BMI = float(new['BMI'])
    PhysicalHealth = float(new['PhysicalHealth'])
    MentalHealth = float(new['MentalHealth'])
    Smoking = content['Smoking']
    AlcoholDrinking = content['AlcoholDrinking']
    Stroke = content['Stroke']
    DiffWalking = content['DiffWalking']
    Sex = content['Sex']
    PhysicalActivity = content['PhysicalActivity']
    Asthma = content['Asthma']
    KidneyDisease = content['KidneyDisease']
    SkinCancer = content['SkinCancer']
    AgeCategory = content['AgeCategory']
    Race = content['Race']
    Diabetic = content['Diabetic']
    GenHealth = content['GenHealth']

    prediction = modelHelper.makePredictions( BMI, PhysicalHealth, MentalHealth, Smoking, 
    AlcoholDrinking, Stroke, DiffWalking, Sex, PhysicalActivity, Asthma, KidneyDisease,SkinCancer,
     AgeCategory, Race, Diabetic, GenHealth )
    print(prediction)

    return(jsonify({"ok": True, "prediction": str(prediction)}))

#####################################################################
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

#main
if __name__ == "__main__":
    app.run(debug=True)
