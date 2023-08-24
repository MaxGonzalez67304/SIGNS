from flask import Flask, jsonify, request, Response
from pymongo import MongoClient
from bson.objectid import ObjectId

import os
from os import path

import Apis.GlobalInfo.ResponseMessages as ResponseMessages

import Apis.GlobalInfo.Keys as Keys

import Apis.GlobalInfo.Helpers as Helpers

import base64

dbConnection = None

# Connection to MongoDB
if Keys.strConnection != None:
    mongoConnect = MongoClient(Keys.strConnection)
    Keys.dbConnection = mongoConnect[Keys.strDBConection]
    dbConnection = Keys.dbConnection

def fnGetAllPalabras():
    try:
        jsnProyection = {'_id': 0}
        cursor = dbConnection.palabras.find({}, jsnProyection)
        objResult = []

        for document in cursor:
            objResult.append(document)
            print(document)

        return {'intStatus': 200, 'strAnswer': objResult}
    except Exception as e:
        Helpers.PrintException()
        return jsonify(ResponseMessages.err500)



