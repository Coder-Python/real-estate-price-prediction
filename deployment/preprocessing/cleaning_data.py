"""
In the preprocessing/ folder:
Create the cleaning_data.py file that will contain all the code that will be used to preprocess the data you will receive to predict a new price. (fill the NaN values, handle text data, one-hot encode the caterogical features, normalize the continuous data, etc...).
This file should contain a function called preprocess() that will take a new house's data as input and return those data preprocessed as output.
If your data doesn't contain the required information, you should return an error to the user.
"""

def preprocess(data):
    living_area = data['data']['Living_Area']
    type_of_property = data['data']['Type_of_property']
    number_of_rooms = data['data']['Number_of_rooms']
    locality = data['data']['Locality']

    # Perform data cleaning and preprocessing
    if type_of_property == "HOUSE":
        type_of_property = 3
    elif type_of_property == "APARTMENT":
        type_of_property = 1
    else:
        type_of_property = 3
    
    processed_data = [living_area, type_of_property, number_of_rooms, locality]
    
    return processed_data


