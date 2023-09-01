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
    """
    Recupera todas las palabras en la base de datos.

    Returns:
    - intStatus: Estado de la petición HTTP exitosa.
    - strAnswer: Objeto resultante con la información de la base de datos.
    """
    try:
        cursor = dbConnection.palabras.find({}, PROYECTION)

        objResult = [document for document in cursor]

        return {'intStatus': 200, 'strAnswer': objResult}
    except Exception as error:
        logging.exception("Error en fnGetAllPalabras: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


def fnGetPalabraByNombre(palabra):
    """
    Recupera una palabra según su nombre en la base de datos.

    Parámetros:
    - palabra (string): El nombre de la palabra a buscar.

    Returns:
    - intStatus: Estado de la petición HTTP exitosa.
    - strAnswer: Objeto resultante con la información de la base de datos.
    """
    try:
        if not palabra:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"palabra": palabra}
        cursor = dbConnection.palabras.find_one(jsnQuery, PROYECTION)
        objResult = cursor

        return {'intStatus': http.HTTPStatus.OK, 'strAnswer': objResult}
    except Exception as error:
        logging.exception("Error en fnGetPalabraByNombre: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


def fnPostPalabra(strPalabra, strVideo):
    """
    Agrega una palabra y su respectivo video a la base de datos.

    Parámetros:
    - strPalabra (string): El nombre de la palabra a agregar.
    - strVideo (string): El video de la palabra a agregar.

    Returns:
    - intStatus: Estado de la petición HTTP exitosa.
    - strAnswer: Mensaje de información agregada correctamente.
    """
    try:
        if not strPalabra or not strVideo:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"palabra": strPalabra, "video": strVideo}
        dbConnection.palabras.insert_one(jsnQuery)

        return {'intStatus': 200, 'strAnswer': "Palabra insertada correctamente"}
    except Exception as error:
        logging.exception("Error en fnPostPalabra: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


def fnUpdatePalabraById(objectId, strPalabra, strVideo):
    """
    Actualiza una palabra y su respectivo video en la base de datos.

    Parámetros:
    - objectId (string): El id de la palabra a actualizar.
    - strPalabra (string): El nombre de la palabra a actualizar.
    - strVideo (string): El video de la palabra a actualizar.

    Returns:
    - intStatus: Estado de la petición HTTP exitosa.
    - strAnswer: Mensaje de información actualizada correctamente.
    """
    try:
        if not objectId:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"_id": ObjectId(objectId)}
        cursor = {"$set": {"palabra": strPalabra, "video": strVideo}}
        dbConnection.palabras.update_one(jsnQuery, cursor)

        return {'intStatus': 200, 'strAnswer': "Palabra actualizada correctamente"}
    except Exception as error:
        logging.exception("Error en fnUpdatePalabra: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


def fnDeletePalabraById(objectId):
    """
    Elimina una palabra y su respectivo video en la base de datos.

    Parámetros:
    - objectId (string): El id de la palabra a eliminar.

    Returns:
    - intStatus: Estado de la petición HTTP exitosa.
    - strAnswer: Mensaje de información eliminada correctamente.
    """
    try:
        if not ObjectId.is_valid(objectId):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        jsnQuery = {"_id": ObjectId(objectId)}
        cursor = dbConnection.palabras.delete_one(jsnQuery)

        if cursor.deleted_count == 0 or not cursor:
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return {'intStatus': 200, 'strAnswer': "Palabra eliminada correctamente"}
    except Exception as error:
        logging.exception("Error en fnDeletePalabra: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR
