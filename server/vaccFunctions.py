from flask import Blueprint, request, jsonify
import ssl
from client_functions.py import send_request
from urllib.request import urlretrieve
import tempfile
import shutil

# prevent any ssl issues
ssl._create_default_https_context = ssl._create_unverified_context

VaccFunctions = Blueprint('grayscale', __name__)

@VaccFunctions.route("/vaccFunctions/returnTwelve", methods=['POST'])
def returnTwelve():
    return jsonify({"hello": 12})

@VaccFunctions.route("/test", methods=['POST'])
def testReq():
    req_data = request.get_json()
    data = req_data["countries"]
    return jsonify(data)

@VaccFunctions.route("/vaccFunctions/check", methods=['POST'])
def check():
    #UserID, Countries, States, numDays, Vaccine, Efficacy, numVaccs, numIterations
    req_data = request.get_json()
    efficacy = 0
    vaccine = req_data["Vaccine"]
    vaccine = vaccine[0:3]
    if vaccine == "Comi":
        efficacy = 95.0
    elif vaccine == "mRNA":
        efficacy = 94.1
    elif vaccine == "Coro":
        efficacy = 78.0
    elif vaccine == "AZD1":
        efficacy = 70.4
    elif vaccine == "Sput":
        efficacy = 94.1
    #elif vaccine == "BBIB":
        #efficacy = 79.3
    else:
        return jsonify({"error": "Vaccine name not valid."})
    if req_data["numDays"] < 1 or req_data["numDays"] > 180:
        return jsonify({"error": "Number of days not valid."})
    if req_data["numVaccs"] < 0 or req_data["numVaccs"] > 20000000:
        return jsonify({"error": "Number of vaccines not valid."})
    iterations = 1000 #Default value
    html = send_request(req_data["Countries"], req_data["States"], req_data["numVaccs"], efficacy, req_data["numDays"], iterations, req_data["UserID"])
    return jsonify(html)
