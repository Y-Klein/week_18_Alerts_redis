import json


def get_data():
    with open("../data/border_alerts.json") as file:
        file = json.load(file)
    for doc in file:
        if (((doc["weapons_count"] > 0)
            or (doc["distance_from_fence_m"] <= 50)
            or (doc["people_count"] >= 8))
            or (doc["vehicle_type"] == "truck")):
            doc["priority"] = "URGENT"
        elif ((doc["distance_from_fence_m"] <= 150 and doc["people_count"] >= 4)
          or (doc["vehicle_type"] == "jeep" and doc["people_count"] >= 3)):
            doc["priority"] = "URGENT"

        else:
            doc["priority"] = "NORMAL"
    return file

