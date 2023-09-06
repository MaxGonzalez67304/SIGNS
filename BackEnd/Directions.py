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


@app.route('/api/general/getAllPalabras', methods=['GET'])
def GetAllPalabras() -> jsonify:
    """
    Recupera todos los datos de la colección 'palabras' en la base de datos.

    Returns:
    - objResult: El objeto JSON recibido de fnGetAllPalabras.

    Raises:
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        objResult = callMethod.fnGetAllPalabras()

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetAllPalabras: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/general/getPalabraByNombre/<string:palabra>', methods=['GET'])
def GetPalabraByNombre(palabra) -> jsonify:
    """
    Recupera una palabra en base a su nombre.

    Parámetros:
    - palabra (string): El nombre de la palabra a buscar.

    Returns:
    - objResult: El objeto JSON recibido de fnGetPalabraByNombre.

    Raises:
    - 400 Bad Request: Si el campo 'palabra' no está en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        if not palabra:
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnGetPalabraByNombre(palabra)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetPalabraById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/general/postPalabra', methods=['POST'])
def PostPalabra() -> jsonify:
    """
    Agrega una palabra y un video a la base de datos.

    Returns:
    - objResult: El objeto JSON recibido de fnPostPalabra.

    Raises:
    - 400 Bad Request: Si los campos 'palabra' o 'video' no están en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        json_data = request.json
        palabra = json_data.get('palabra', None)
        video = json_data.get('video', None)

        if not palabra or not video or not isinstance(palabra, str) or not isinstance(video, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnPostPalabra(palabra, video)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en PostPalabra: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/general/updatePalabraById/<string:_id>', methods=['PUT'])
def updatePalabraById(_id) -> jsonify:
    """
    Actualiza una palabra en base a su id.

    Parámetros:
    - _id (string): El id de la palabra a actualizar.

    Returns:
    - objResult: El objeto JSON recibido de fnUpdatePalabraById.

    Raises:
    - 400 Bad Request: Si los campos 'palabra' o 'video' no están en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        json_data = request.json
        palabra = json_data.get('palabra', None)
        video = json_data.get('video', None)

        if not palabra or not video or not isinstance(_id, str) or not isinstance(palabra, str) or not isinstance(video, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnUpdatePalabraById(_id, palabra, video)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en updatePalabraById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR


@app.route('/api/general/deletePalabraById/<string:_id>', methods=['DELETE'])
def deletePalabraById(_id) -> jsonify:
    """
    Elimina una palabra en base a su id.

    Parámetros:
    - _id (string): El id de la palabra a eliminar.

    Returns:
    - objResult: El objeto JSON recibido de fnDeletePalabraById.

    Raises:
    - 400 Bad Request: Si el campo '_id' no está en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a eliminar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        if not _id or not isinstance(_id, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnDeletePalabraById(_id)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en deletePalabraById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/getAllUsuarios', methods=['GET'])
def GetAllUsuarios() -> jsonify:
    """
    Recupera todos los datos de la colección 'usuarios' en la base de datos.

    Returns:
    - objResult: El objeto JSON recibido de fnGetAllUsuarios.

    Raises:
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        objResult = callMethod.fnGetAllUsuarios()

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetAllUsuarios: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/getUsuarioById/<string:_id>', methods=['GET'])
def GetUsuarioById(_id) -> jsonify:
    """
    Recupera un usuario en base a su id.

    Parámetros:
    - _id (string): El id del usuario a buscar.

    Returns:
    - objResult: El objeto JSON recibido de fnGetUsuarioById.

    Raises:
    - 400 Bad Request: Si el campo '_id' no está en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        if not _id or not isinstance(_id, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnGetUsuarioById(_id)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en GetUsuarioById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/postUsuario', methods=['POST'])
def PostUsuario() -> jsonify:
    """
    Agrega un usuario a la base de datos.

    Returns:
    - objResult: El objeto JSON recibido de fnPostUsuario.

    Raises:
    - 400 Bad Request: Si los campos 'nombre', 'username', 'correo' o 'password' no están en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        json_data = request.json
        nombre = json_data.get('nombre', None)
        correo = json_data.get('correo', None)
        username = json_data.get('username', None)
        password = json_data.get('password', None)

        if not nombre or not username or not correo or not password or not isinstance(nombre, str) or not isinstance(username, str) or not isinstance(correo, str) or not isinstance(password, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnPostUsuario(nombre, username, correo, password)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en PostUsuario: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/updateUsuarioById/<string:_id>', methods=['PUT'])
def updateUsuarioById(_id) -> jsonify:
    """
    Actualiza un usuario en base a su id.

    Parámetros:
    - _id (string): El id del usuario a actualizar.

    Returns:
    - objResult: El objeto JSON recibido de fnUpdateUsuarioById.

    Raises:
    - 400 Bad Request: Si los campos 'nombre', 'username', 'correo' o 'password' no están en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a actualizar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        json_data = request.json
        nombre = json_data.get('nombre', None)
        correo = json_data.get('correo', None)
        username = json_data.get('username', None)
        password = json_data.get('password', None)

        if not nombre or not username or not correo or not password or not isinstance(_id, str) or not isinstance(nombre, str) or not isinstance(username, str) or not isinstance(correo, str) or not isinstance(password, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnUpdateUsuarioById(_id, nombre, correo, username, password)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en updateUsuarioById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

@app.route('/api/general/deleteUsuarioById/<string:_id>', methods=['DELETE'])
def deleteUsuarioById(_id) -> jsonify:
    """
    Elimina un usuario en base a su id.

    Parámetros:
    - _id (string): El id del usuario a eliminar.

    Returns:
    - objResult: El objeto JSON recibido de fnDeleteUsuarioById.

    Raises:
    - 400 Bad Request: Si el campo '_id' no está en la petición JSON.
    - 404 Not Found: Si no se encontró el id de la palabra a eliminar.
    - 500 Internal Server Error: Si ocurre un error en el servidor.
    """
    try:
        if not _id or not isinstance(_id, str):
            return jsonify(ResponseMessages.err400), http.HTTPStatus.BAD_REQUEST

        objResult = callMethod.fnDeleteUsuarioById(_id)

        if not objResult or not isinstance(objResult, dict):
            return jsonify(ResponseMessages.err404), http.HTTPStatus.NOT_FOUND

        return jsonify(objResult)
    except Exception as error:
        logging.exception("Error en deleteUsuarioById: %s", error)
        return jsonify(ResponseMessages.err500), http.HTTPStatus.INTERNAL_SERVER_ERROR

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9005, debug=True, threaded=True)
