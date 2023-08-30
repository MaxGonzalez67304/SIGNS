from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId

import os
from os import path

import logging
import http
import Apis.GlobalInfo.ResponseMessages as ResponseMessages
import Apis.GlobalInfo.Keys as Keys
import base64

dbConnection = None

PROYECTION = {'_id': 0}

# Connection to MongoDB
if Keys.strConnection != None:
    mongoConnect = MongoClient(Keys.strConnection)
    Keys.dbConnection = mongoConnect[Keys.strDBConection]
    dbConnection = Keys.dbConnection

def fnGetAllPalabras():
    try:
        cursor = dbConnection.palabras.find({}, PROYECTION)

        objResult = [document for document in cursor]

        return {'intStatus': 200, 'strAnswer': objResult}
    except Exception as error:
        logging.exception("Error en fnGetAllPalabras: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

def fnGetPalabraByNombre(palabra):
    """
    Recupera una palabra según su nombre en la base de datos.

    Parámetros:
    - palabra (str): El nombre de la palabra a buscar.

    Returns:
    - intStatus: Estado de la petición HTTP xitosa.
    - strAnswer: Respuesta de la petición HTTP exitosa.
    """
    try:
        if not palabra:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"palabra": palabra}
        cursor = dbConnection.palabras.find_one(jsnQuery, PROYECTION)
        objResult = cursor

        return {'intStatus': http.HTTPStatus.OK, 'strAnswer': objResult}
    except Exception as error:
        logging.exception("Error en fnGetPalabraByNombre: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

def fnPostPalabra(strPalabra, strVideo):
    try:
        if not strPalabra or not strVideo:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"palabra": strPalabra, "video": strVideo}
        dbConnection.palabras.insert_one(jsnQuery)

        return {'intStatus': 200, 'strAnswer': "Palabra insertada correctamente"}
    except Exception as error:
        logging.exception("Error en fnPostPalabra: {}".format(error))
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR
