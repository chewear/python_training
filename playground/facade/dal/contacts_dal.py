from util.file_util import read_json_as_dict

def retrieve_contacts():
    return read_json_as_dict("contacts.json")
    