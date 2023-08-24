from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId

import os
from os import path

import logging

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
        logging.exception(error)
        return jsonify(ResponseMessages.err500), 500

def fnGetPalabraById(idPalabra):
    try:
        jsnQuery = {"idPalabra": idPalabra}
        cursor = dbConnection.palabras.find_one(jsnQuery, PROYECTION)
        objResult = cursor

        return {'intStatus': 200, 'strAnswer': objResult}
    except Exception as error:
        logging.exception(error)
        return jsonify(ResponseMessages.err500), 500

