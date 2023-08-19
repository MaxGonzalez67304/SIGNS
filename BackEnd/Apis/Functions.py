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



