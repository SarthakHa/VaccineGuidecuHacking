from flask import Blueprint, request, jsonify
import ssl
from client_functions import send_request, check_existence
from urllib.request import urlretrieve
import tempfile
import shutil
import time
import json
import numpy as np

# prevent any ssl issues
ssl._create_default_https_context = ssl._create_unverified_context

VaccFunctions = Blueprint('grayscale', __name__)

@VaccFunctions.route("/vaccFunctions/returnTwelve", methods=['POST'])
def returnTwelve():
    return jsonify({"hello": 12})

@VaccFunctions.route("/test", methods=['POST'])
def testReq():
    req_data = request.get_json()
    return jsonify({"test": 12})

@VaccFunctions.route("/vaccFunctions/check", methods=['POST'])
def checkInitial():
    #UserID, Countries, States, numDays, Vaccine, Efficacy, numVaccs, numIterations
    '''
    req_data = request.get_json()
    efficacy = 0
    vaccine = req_data["Vaccine"]
    efficacy = vaccine
    #Processing countries input
    countries = req_data["Countries"]
    for i in range(len(countries)):
        countries[i] = countries[i].replace(" ", "_")
    #Processing states input
    states = req_data["States"]
    if states == "":
        states = []
    else:
        for i in range(len(states)):
            states[i] = states[i].replace(" ", "_")
    #Error checking
    if len(countries) < 3 and len(states) < 3:
        return jsonify({"error": "Select fewer countries."})
    if req_data["numDays"] < 1 or req_data["numDays"] > 180:
        return jsonify({"error": "Number of days not valid."})
    if req_data["numVaccs"] < 0 or req_data["numVaccs"] > 20000000:
        return jsonify({"error": "Number of vaccines not valid."})
    iterations = 100 #Default value
    port_no = send_request(req_data["Countries"], states, req_data["numVaccs"], efficacy, req_data["numDays"], iterations, req_data["UserID"])
    html = "http://128.2.178.158:" + str(port_no)
    return jsonify({"url": html})
    '''
    return jsonify({"test": "yes"})

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray) or isinstance(obj,np.int64):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

@VaccFunctions.route("/vaccFunctions/continualCheck", methods=["POST"])
def continualCheck():
    '''
    req_data = request.get_json()
    uid = req_data["UserID"]
    while True:
        time.sleep(5)
        data = check_existence(uid, "policy_data.npy")
        if len(data) != 0:
            json_dump = json.dumps(data, cls=NumpyEncoder)
            return json_dump
    '''
    data = np.load("../model_fitting/test_data/policy_data1.npy", allow_pickle=True).item()
    json_dump = json.dumps(data, cls=NumpyEncoder)
    #print(json_dump)
    return json_dump
