"""
This function automatically downloads the necessary data, trains two different models,
and deploys a Flask server which listens for POST requests on port 5000.

Author: Richard Galvez
"""

import h2o
import flask
from flask import Flask, request, jsonify
from model_training.training import train_models
from model_predict.prediction import predict

h2o.init()
h2o.remove_all()

# Where to find the source data:
training_file_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx'
models = train_models(data_url=training_file_url, train_fraction=0.8, max_train_time=30)

app = Flask(__name__)

@app.route('/', methods=['POST'])
def post_route():
    if request.method == 'POST':

        x = request.get_json(force=True)
        x = h2o.H2OFrame(x)
        y = predict(x, models)

        result_dict = {'Y1': y[0], 'Y2': y[1]}
        return jsonify(result_dict)

# running on 0.0.0.0 is necessary for the server process to adequately listen on port 5000.
app.run(host='0.0.0.0')

# example input: '{"X1": 0.98, "X2": 514.5, "X3": 294, "X4": 110.25, "X5": 7, "X6": 4, "X7": 0, "X8": 0}'