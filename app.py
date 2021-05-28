from flask import Flask, jsonify, request

application = Flask(__name__)

@application.route('/', methods =['GET'])
def home():
    return "Seja Bem Vindo ao VNCS-13",200
