from flask_cors import CORS, cross_origin

import os
import sys
import logging
import Apis.Functions as callMethod

import Apis.GlobalInfo.Keys as Keys

import Apis.GlobalInfo.ResponseMessages as ResponseMessages

from flask import Flask, jsonify, request, Response

app = Flask(__name__)
CORS(app)

@app.route('/api/general/GetAllPalabras', methods=['GET'])
def GetAllPalabras():
    try:
        objResult = callMethod.fnGetAllPalabras()
        if objResult is None or len(objResult) == 0:
            return jsonify(ResponseMessages.err404), 404

        return jsonify(objResult)
    except Exception as error:
        logging.exception(error)
        return jsonify(ResponseMessages.err500), 500

@app.route('/api/general/GetPalabraById/<int:idPalabra>', methods=['GET'])
def GetPalabraById(idPalabra):
    try:
        objResult = callMethod.fnGetPalabraById(idPalabra)
        if objResult is None or len(objResult) == 0:
            return jsonify(ResponseMessages.err404), 404
        return jsonify(objResult)
    except Exception as error:
        logging.exception(error)
        return jsonify(ResponseMessages.err500), 500



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9005, debug=True, threaded=True)
