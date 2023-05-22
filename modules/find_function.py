import json
import os

def find_function(function_name):
    with open("../Settings/locations_function.json", "r") as file:
        functions = json.load(file)
        file_path = functions.get(function_name, {}).get("file_path")
        if file_path:
            root_dir = os.path.dirname(os.path.abspath(__file__))
            module_dir = os.path.join(root_dir, "Modules")
            return os.path.join(module_dir, file_path)
        else:
            return "Function not found"

function_location = find_function("find_location")
print(function_location)
