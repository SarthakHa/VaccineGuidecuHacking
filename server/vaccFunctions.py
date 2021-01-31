from flask import Blueprint, request, jsonify
import ssl
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
    data = req_data["ID"]
    return jsonify({"hello": 12})

@VaccFunctions.route("/vaccFunctions/check", methods=['POST'])
def check():
    req_data = request.get_json()
    data = req_data["ID"]
    return jsonify({"ID": data})
