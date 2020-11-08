from flask import Flask, request, Response
from flask.json import dumps
import mariadb
import json
import random

app = Flask(__name__)

list = [("snake, dog, cat")]
list2 = [("snake, dog, cat, monkey")]

@app.route ('/animals', methods=['POST', 'GET', 'DELETE', 'PATCH'])   
def list_animals():
    if request.method == "GET":
        return Response (list, mimetype="json/application", status=201)
    elif request.method == "POST":
        return Response(list2 ,mimetype="json/application", status=205)
    elif request.method == "DELETE":
        return Response("You've deleted the Snake", mimetype="json/application", status=205)
    elif request.method == "PATCH":
        return Response("The Dog is now a Bassett Hound", mimetype="json/application", status=205)