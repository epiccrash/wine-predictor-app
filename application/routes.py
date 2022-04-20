from application import app
from flask import render_template, request, json, jsonify
import requests

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/enterQualityInfo", methods=['GET', 'POST'])
def enterQualityInfo():
    return render_template("index.html", is_data_entered=True)


@app.route("/predictQuality", methods=['GET', 'POST'])
def predictQuality():
    # Form inputs
    fixedAcidity = request.form.get("fixedAcidity")
    volatileAcidity = request.form.get("volatileAcidity")
    citricAcid = request.form.get("citricAcid")
    freeSulfurDioxide = request.form.get("freeSulfurDioxide")
    totalSulfurDioxide = request.form.get("totalSulfurDioxide")
    sulfates = request.form.get("sulfates")
    alcohol = request.form.get("alcohol")
    wineType = request.form.get("wineType")

    # Convert data to JSON
    info = json.dumps({
        "fixedAcidity": fixedAcidity, 
        "volatileAcidity": volatileAcidity, 
        "citricAcid": citricAcid, 
        "freeSulfurDioxide": freeSulfurDioxide, 
        "totalSulfurDioxide": totalSulfurDioxide, 
        "sulfates": sulfates, 
        "alcohol": alcohol,
        "wineType": wineType
    })

    # URL for model
    url = "https://wine-club-model.herokuapp.com/api"
    # url = "http://localhost:3000/api"
  
    # Post to model
    results = requests.post(url, info)

    return render_template("index.html", is_predict_quality=True, fixedAcidity = fixedAcidity, volatileAcidity = volatileAcidity, citricAcid = citricAcid, freeSulfurDioxide = freeSulfurDioxide, totalSulfurDioxide = totalSulfurDioxide, sulfates = sulfates, alcohol = alcohol, results=results.content.decode('UTF-8'), info=info)
