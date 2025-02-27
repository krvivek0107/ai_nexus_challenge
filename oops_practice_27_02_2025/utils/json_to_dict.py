import json
import os

class Json_to_dict:
    def __init__(self):
        pass

    def fecth_data_from_json(self):
        json_data_in_dict = {}
        with open(rf"{os.getcwd()}\path_config\config.json") as fp:
            json_data_in_dict = json.load(fp)
        return json_data_in_dict