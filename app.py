import flask
import json
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)


@app.route('/', methods=['POST', 'GET'])
def home():
    return "Hello!"
#function to cehck the actual state of the reset or not
@app.route('/get_reset_info', methods=['POST', 'GET'])
def get_reset_info():
        
    # ChessBoard_info = pd.read_csv("ChessBoard_info.csv")
    ChessBoard_info = pd.read_json("reset_state.json")
    reset_command = ChessBoard_info#ChessBoard_info.loc[ChessBoard_info['reset']]
    
    out = reset_command.to_dict(orient = "records")
    
    # resp = flask.jsonify(out[0])
    # resp = flask.jsonify(out)

    # Opening JSON file
    f = open('reset_state.json',)
    
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list

    
    resp = flask.jsonify(data)
    # Closing file
    f.close()
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/set_reset_info', methods=['POST', 'GET'])
def set_reset_info():
    post_request = request.get_json(force=True) # Get data posted as a json
    name_state='reset'
    state = int(post_request[name_state])
    #cehcking if reset state exist
    if  not (name_state in post_request )and type(post_request[name_state] ) != int:
        resp = flask.jsonify("No Reset state provided")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    
    ChessBoard_info = pd.read_csv("ChessBoard_info.csv")
    ChessBoard_info['reset']=state
    
    out = ChessBoard_info.to_dict(orient = "reset")
    
    resp = flask.jsonify(out[0])
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp


@app.route('/get_test_results', methods=['POST', 'GET'])
def get_test_results():
    post_request = request.get_json(force=True) # Get data posted as a json
    id = int(post_request['patient_id'])
    if not id:
        resp = flask.jsonify("No ID provided")
        resp.headers.add('Access-Control-Allow-Origin', '*')
        return resp
    
    patients_results = pd.read_csv("patient_results.csv")
    patient_results = patients_results.loc[patients_results['patient_id'] == id]
    
    out = patient_results.to_dict(orient = "records")
    
    resp = flask.jsonify(out[0])
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

if __name__ == '__main__':
    app.run(port=5500)
