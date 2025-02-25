import os

from datetime import date

def create_file_name_city(city, path, file_type):
    os.chdir(path)
    avl_files = os.listdir(path)
    today = date.today()
    file_name = f"{city}_{today}.csv"
    if file_name not in avl_files:
        os.system(f"""echo "{file_type}" > {file_name}""")
