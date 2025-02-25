import csv
from datetime import date
from data_segregation_param_city.utils.path_config import input_folder_path, input_daily_files, output_path, output_folder_name

def process_file(file):
    with open(rf"{input_folder_path}\{input_daily_files}\{file}") as fp:
        records = csv.reader(fp)
        for record in records:
            city = record[2]
            with open(rf"{output_path}\{output_folder_name}\{city}_{date.today()}.csv", 'a') as fp1:
                writer = csv.writer(fp1)
                writer.writerow(record)






