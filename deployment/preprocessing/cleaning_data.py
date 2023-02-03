# Data preprocessing
def preprocess(data):
    living_area = data["data"]["Living_Area"]
    type_of_property = data["data"]["Type_of_property"]
    number_of_rooms = data["data"]["Number_of_rooms"]
    locality = data["data"]["Locality"]

    # Perform data cleaning and preprocessing
    if type_of_property == "HOUSE":
        type_of_property = 3
    elif type_of_property == "APARTMENT":
        type_of_property = 1
    else:
        type_of_property = 3

    processed_data = [living_area, type_of_property, number_of_rooms, locality]

    return processed_data
