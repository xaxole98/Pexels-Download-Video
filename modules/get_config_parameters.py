from execute_function import execute_function
import json

params = {}

def get_parameters(parameter_name):
    global params
    if parameter_name in params:
        return params[parameter_name]

    location = execute_function("find_location", parameter_name)
    with open(location, "r") as file:
        data = json.load(file)
        params[parameter_name] = data[parameter_name]
        return data[parameter_name]

api_keys = get_parameters("ApiKeys")
sound = get_parameters("sound")
language = get_parameters("language")
media_type = get_parameters("media_type")
orientation = get_parameters("orientation")
size = get_parameters("size")
page = get_parameters("page")
per_page = get_parameters("per_page")
query = get_parameters("query")
save = get_parameters("save")
resolution = get_parameters("resolution")
typedownload = get_parameters("typedownload")

