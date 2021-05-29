from flask import Flask, jsonify, request

application = Flask(__name__)

@application.route('/')
def home():
    return "Seja Bem Vindo ao VNCS-13"
