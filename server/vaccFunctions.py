from flask import Blueprint, request, jsonify
import ssl
from client_functions import send_request
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
    data = req_data["Countries"]
    return jsonify(data)

@VaccFunctions.route("/vaccFunctions/check", methods=['POST'])
def check():
    #UserID, Countries, States, numDays, Vaccine, Efficacy, numVaccs, numIterations
    req_data = request.get_json()
    efficacy = 0
    vaccine = req_data["Vaccine"]
    efficacy = vaccine
    if req_data["numDays"] < 1 or req_data["numDays"] > 180:
        return jsonify({"error": "Number of days not valid."})
    if req_data["numVaccs"] < 0 or req_data["numVaccs"] > 20000000:
        return jsonify({"error": "Number of vaccines not valid."})
    iterations = 1000 #Default value
    html = send_request(req_data["Countries"], req_data["States"], req_data["numVaccs"], efficacy, req_data["numDays"], iterations, req_data["UserID"])
    return jsonify(html)
