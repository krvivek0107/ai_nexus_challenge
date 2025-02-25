from data_segregation_param_city.business_logic.daily_run import process_invalid_files, process_file_param_city
from data_segregation_param_city.utils.create_folder_on_fly import create_output_folder
from data_segregation_param_city.utils.segregate_file_param_extension import segregate_file
from data_segregation_param_city.utils.path_config import input_folder_path, input_daily_files
import os

def get_aval_files(folder_path):
    aval_files = os.listdir(folder_path)
    return aval_files

def segregate_files_param_extension(file_type, aval_files):
    process_invalid_files(file_type, aval_files)
    process_file_param_city(segregate_file(file_type, aval_files))


def main():
    input_path = rf"{input_folder_path}\{input_daily_files}"
    aval_files = get_aval_files(input_path)
    file_type = ".csv"
    create_output_folder()
    segregate_files_param_extension(file_type, aval_files)

if __name__ == "__main__":
    main()
    print("process_ends")
