from flask import Flask, render_template, jsonify, send_from_directory, request
import json
import pandas as pd
import numpy as np
import os

#init app and class
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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
