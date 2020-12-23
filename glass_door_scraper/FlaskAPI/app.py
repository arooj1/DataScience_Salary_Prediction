import flask
from flask import Flask, jsonify, request
import json
import pickle
import numpy as np

from data_input import data_in
app = Flask(__name__)


def load_models():
    file_name = "models/salary_model.p"
    with open(file_name, 'rb') as pickled:
        data = pickle.load(pickled)
        model = data['model']
    return model


@app.route('/predict', methods=['GET'])
def predict():
# stub input features
    #x = np.array(data_in).reshape(1,-1)
    #x.shape
# parse input features from request
    request_json = request.get_json()
    x = (request_json['input'])
    x_in = np.array(data_in).reshape(1,-1)
    
# load model
    model = load_models()
    prediction = model.predict(x_in)[0]
    print('data loaded from the server: Prediction: ', prediction)
    response = json.dumps({'response': prediction})
    return response, 200
if __name__ == '__main__':
    
    application.run(debug=True)
