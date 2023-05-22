from find_location import find_location
import json

def execute_function(function_name, *args, **kwargs):
    if function_name == "find_location":
        return find_location(*args, **kwargs)
    else:
        function = find_function(function_name)
        if function == "Function not found":
            print("Function not found")
            return
        return function(*args, **kwargs)
