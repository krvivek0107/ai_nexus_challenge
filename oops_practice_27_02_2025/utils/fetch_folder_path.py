import os
from oops_practice_27_02_2025.utils.json_to_dict import Json_to_dict

class Fetch_folder_path:
    def __init__(self):
        self.obj = Json_to_dict()

    def fetch_input_folder_path(self):
        return self.obj.fecth_data_from_json()["input_folder_path"]


    def fetch_output_folder_path(self):
        return self.obj.fecth_data_from_json()["output_folder_path"]