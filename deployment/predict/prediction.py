# Prediction with xgboost
import xgboost as xgb


def predict(processed_data):
    # Load the XGBoost model
    model = xgb.XGBRegressor()
    model.load_model("./model/model.bin")

    # Make predictions with the model
    prediction = model.predict([processed_data])

    return prediction
