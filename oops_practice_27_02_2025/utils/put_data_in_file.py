import csv
import os

from oops_practice_27_02_2025.utils.json_to_dict import Json_to_dict
class Put_data:
    def __init__(self, records):
        self.records = records
        self.obj = Json_to_dict()

    def dump_data_in_file(self):
        with open(rf"{self.obj.fecth_data_from_json()["output_folder_path"]}\sol.csv", 'a') as fp:
            csv_writer = csv.writer(fp)
            for record in self.records:
                csv_writer.writerow(record)











