from application import app
from flask import render_template, request, json, jsonify
import requests

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/enterQualityInfo", methods=['GET', 'POST'])
def enterQualityInfo():

    # Form inputs
    fixedAcidity = float(request.form.get("fixedAcidity"))
    volatileAcidity = float(request.form.get("volatileAcidity"))
    freeSulfurDioxide = float(request.form.get("freeSulfurDioxide"))
    totalSulfurDioxide = float(request.form.get("totalSulfurDioxide"))
    alcohol = int(request.form.get("alcohol"))
    wineType = request.form.get("wineType")
    quality = int(request.form.get("quality"))

    # Convert data to JSON
    info = json.dumps({
        "fixedAcidity": fixedAcidity, 
        "volatileAcidity": volatileAcidity,
        "freeSulfurDioxide": freeSulfurDioxide, 
        "totalSulfurDioxide": totalSulfurDioxide,
        "alcohol": alcohol,
        "wineType": wineType,
        "quality": quality
    })

    info = json.loads(info)
    if (wineType == 'red'):
        citricAcid = float(request.form.get("citricAcid"))
        sulfates = float(request.form.get("sulfates"))
        info["citricAcid"] = citricAcid
        info["sulfates"] = sulfates
    else:
        residualSugar = float(request.form.get("residualSugar"))
        chlorides = float(request.form.get("chlorides"))
        info["residualSugar"] = residualSugar
        info["chlorides"] = chlorides

    info = json.dumps(info)

    # URL for model
    # url = "http://localhost:3000/api/getDonatedData"
    url = "https://wine-prediction-web-model.herokuapp.com/api/getDonatedData"
  
    # Post to model
    results = requests.post(url, info)

    info = json.loads(info)

    return render_template("index.html", is_data_entered=True, info=info, results=results.content.decode('UTF-8'))


@app.route("/predictQuality", methods=['GET', 'POST'])
def predictQuality():
    # Form inputs
    fixedAcidity = float(request.form.get("fixedAcidity"))
    volatileAcidity = float(request.form.get("volatileAcidity"))
    freeSulfurDioxide = float(request.form.get("freeSulfurDioxide"))
    totalSulfurDioxide = float(request.form.get("totalSulfurDioxide"))
    alcohol = int(request.form.get("alcohol"))
    wineType = request.form.get("wineType")

    # Convert data to JSON
    info = json.dumps({
        "fixedAcidity": fixedAcidity, 
        "volatileAcidity": volatileAcidity,
        "freeSulfurDioxide": freeSulfurDioxide, 
        "totalSulfurDioxide": totalSulfurDioxide,
        "alcohol": alcohol,
        "wineType": wineType
    })

    info = json.loads(info)
    if (wineType == 'red'):
        print(request.form.get("citricAcid"))
        citricAcid = float(request.form.get("citricAcid"))
        sulfates = float(request.form.get("sulfates"))
        info["citricAcid"] = citricAcid
        info["sulfates"] = sulfates
    else:
        residualSugar = float(request.form.get("residualSugar"))
        chlorides = float(request.form.get("chlorides"))
        info["residualSugar"] = residualSugar
        info["chlorides"] = chlorides

    info = json.dumps(info)

    # URL for model
    # url = "http://localhost:3000/api"
    url = "https://wine-prediction-web-model.herokuapp.com/api"
  
    # Post to model
    results = requests.post(url, info)

    info = json.loads(info)

    return render_template("index.html", is_predict_quality=True, info=info, results=results.json())
