import os

from oops_practice_27_02_2025.utils.ops_on_csv import Ops_csv_file
from oops_practice_27_02_2025.utils.ops_on_txt import Ops_txt_file
from oops_practice_27_02_2025.utils.put_data_in_file import Put_data
from oops_practice_27_02_2025.utils.json_to_dict import Json_to_dict

class Ops_on_file:
    def __init__(self):
        self.obj = Json_to_dict()
        self.all_aval_files = os.listdir(self.obj.fecth_data_from_json()["input_folder_path"])

    def get_data_from_file_and_dump_in_another_file(self):
        for file in self.all_aval_files:
            records = []
            if file.endswith(".csv"):
                obj2 = Ops_csv_file(rf"{self.obj.fecth_data_from_json()["input_folder_path"]}\{file}")
                records = obj2.get_data_from_csv_file()
            elif file.endswith(".txt"):
                obj3 = Ops_txt_file(rf"{self.obj.fecth_data_from_json()["input_folder_path"]}\{file}")
                records = obj3.get_data_from_txt_file()
            else:
                pass

            obj1 = Put_data(records)
            obj1.dump_data_in_file()
