from flask import Flask, jsonify, request

app = Flask(__name__)

state = { "value" : 1} 

@app.route('/', methods =['GET'])
def home():
    return "Seja Bem Vindo ao VNCS-13",200

@app.route('/GetState', methods =['GET'])
def home():
    return jsonify(state),200

@app.route('/AppChangeState', methods =['GET'])
def AppChangeState():
    if state['value'] == 1:
        state['value'] = 0
    else:
        state['value'] = 1

    return jsonify(state),200

@app.route('/NodeChangeState', methods =['POST'])
def NodeChangeState():
    data = request.get_json()
    state.update(data)

    return jsonify(data),201
