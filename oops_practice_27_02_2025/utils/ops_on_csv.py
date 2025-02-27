import csv


class Ops_csv_file:
    def __init__(self, full_file_name):
        self.full_file_name = full_file_name

    def get_data_from_csv_file(self):
        data = []
        with open(self.full_file_name) as fp:
            records = csv.reader(fp) #records is iterator
            for record in records:
                data.append(record)
        return data



