import json
from util.logger import enable_logger

@enable_logger
def read_json_as_dict(file_name: str) -> dict:
    try:
        with open(file_name) as f:
            contents = "".join(f.readlines())
        return json.loads(contents)
    except FileNotFoundError:
        raise Exception(f"File '{file_name}' not found.")


