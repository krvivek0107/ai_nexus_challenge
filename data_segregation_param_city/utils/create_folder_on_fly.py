import os
from data_segregation_param_city.utils.path_config import output_path, output_folder_name
def create_output_folder():
    # path = r"C:\Users\Rohit\Desktop\ai_nexus\data_segregation_param_city"
    # folder_name = "output_data"
    aval_cont = os.listdir(output_path)
    if output_folder_name not in aval_cont:
        prev_loc = rf"{os.getcwd()}"
        os.chdir(output_path)
        os.mkdir(output_folder_name)
        os.chdir(prev_loc)
    else:
        return rf"{output_path}\{output_folder_name}"

    return rf"{output_path}\{output_folder_name}"



