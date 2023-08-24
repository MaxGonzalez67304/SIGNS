from flask_cors import CORS, cross_origin

import os
import sys
import Apis.Functions as callMethod

import Apis.GlobalInfo.Keys as Keys

import Apis.GlobalInfo.Helpers as Helpers

import Apis.GlobalInfo.ResponseMessages as ResponseMessages

from flask import Flask, jsonify, request, Response

app = Flask(__name__)
CORS(app)

@app.route('/api/general/GetAllPalabras', methods=['GET'])
def GetAllPalabras():
    try:
        objResult = callMethod.fnGetAllPalabras()
        return jsonify(objResult)
    except Exception as e:
        Helpers.PrintException()
        return jsonify(ResponseMessages.err500)




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9005, debug=True, threaded=True)
