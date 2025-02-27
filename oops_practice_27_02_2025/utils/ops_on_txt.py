class Ops_txt_file:
    def __init__(self, full_file_name):
        self.full_file_name = full_file_name

    def get_data_from_txt_file(self):
        data = []
        with open(self.full_file_name) as fp:
            data = fp.readlines()

        records = []
        for d in data:
            record = d.split()
            records.append(record)

        return records
