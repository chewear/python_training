# import os
import json

def read_json_as_dict(file_name:str)->dict:
    with open(file_name) as file:
        contents = "".join(file.readlines())
    return json.loads(contents)