"""
In the predict/ folder:
Create the prediction.py file that will contain all the code used to predict a new house's price.
Your file should contain a function predict() that will take your preprocessed data as an input and return a price as output.
"""

import xgboost as xgb

def predict(processed_data):
    # Load the XGBoost model
    model = xgb.XGBRegressor()
    model.load_model('./model/model.bin')

    # Make predictions with the model
    prediction = model.predict([processed_data])
    
    return prediction
