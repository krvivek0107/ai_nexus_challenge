from data_segregation_param_city.utils.segregate_file_param_extension import segregate_file
from data_segregation_param_city.utils.not_required_files import segregate_unwanted_files
from data_segregation_param_city.utils.dump_processed_data import dump_input_data
from data_segregation_param_city.business_logic.process_files_param_city import process_file
from data_segregation_param_city.utils.path_config import input_folder_path, input_daily_files, input_others_files, input_processed_files


#2-> segregate and dump all other files not having that extension in other folder
def process_invalid_files(file_type, aval_files):
    req_files = segregate_unwanted_files(file_type, aval_files)
    for file in req_files:
        full_file_path = rf"{input_folder_path}\{input_daily_files}\{file}"
        full_destination_path = rf"{input_folder_path}\{input_others_files}"
        dump_input_data(full_file_path, full_destination_path)

#3-> process file one by one from input folder
def process_file_param_city(exact_extension_files):
    for file in exact_extension_files:
        process_file(file)
        full_file_path = rf"{input_folder_path}\{input_daily_files}\{file}"
        full_destination_path = rf"{input_folder_path}\{input_processed_files}"
        dump_input_data(full_file_path, full_destination_path)

