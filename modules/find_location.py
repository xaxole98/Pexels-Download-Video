import json
import os

def find_location(variable_name):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'settings', 'location.json')
    with open(file_path, "r") as file:
        data = json.load(file)
        location = data.get(variable_name + "_savelocation")
        if location:
            return os.path.join(base_dir, location)
        else:
            return "Location not found"

