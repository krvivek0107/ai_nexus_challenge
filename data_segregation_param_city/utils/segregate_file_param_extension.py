def segregate_file(file_type, aval_files):
    req_files = []
    for file in aval_files:
        if file.endswith(file_type):
            req_files.append(file)
    return req_files