def segregate_unwanted_files(file_type, aval_files):
    others = []
    for file in aval_files:
        if not file.endswith(file_type):
            others.append(file)
    return others
