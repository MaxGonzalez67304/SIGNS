from flask_cors import CORS, cross_origin

import os
import sys
import http
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

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetAllPalabras: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/GetPalabraByNombre/<string:palabra>', methods=['GET'])
def GetPalabraByNombre(palabra):
    try:
        if not palabra:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnGetPalabraByNombre(palabra)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetPalabraById: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/PostPalabra', methods=['POST'])
def PostPalabra():
    try:
        json_data = request.json
        palabra = json_data.get('palabra', None)
        video = json_data.get('video', None)

        if not palabra or not video:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnPostPalabra(palabra, video)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en PostPalabra: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9005, debug=True, threaded=True)
