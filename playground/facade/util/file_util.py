import os
import json

def read_json_as_dict(file_name:str)->dict:
    with open(file_name):
        contents = "".join(file_name.readlines)
    return json.loads(contents)
