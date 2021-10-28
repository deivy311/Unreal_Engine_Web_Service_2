import flask
import json
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
# import trafilatura
from googlesearch import search 
app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, support_credentials=True)


@app.route('/', methods=['POST', 'GET'])
def home():
    return "Hello!"


@app.route('/get_reset_info', methods=['POST', 'GET'])
def get_reset_info():
        
    ChessBoard_info = pd.read_csv("ChessBoard_info.csv")
    patient_info = ChessBoard_info.loc[ChessBoard_info['reset']]
    
    out = patient_info.to_dict(orient = "records")
    
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
