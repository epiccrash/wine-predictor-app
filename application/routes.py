from application import app
from flask import render_template, request, json, jsonify
import requests

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/enterQualityInfo")
def enterQualityInfo():
    return render_template("index.html", is_data_entered=True)

@app.route("/predictQuality")
def predictQuality():
    return render_template("index.html", is_predict_quality=True)
