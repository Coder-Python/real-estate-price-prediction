from flask import Flask, request
import json
from preprocessing.cleaning_data import preprocess
from predict.prediction import predict

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Alive !</h1>"


@app.route('/predict', methods=['GET', 'POST'])
def pred():
    if request.method == 'POST':
        data = request.get_json()
        processed_data = preprocess(data)
        prediction = predict(processed_data)
        
        # Return the prediction in JSON format
        return json.dumps({'prediction': int(prediction.tolist()[0])})
    else:
        return "<h1>Please use POST method !</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
