def read_text_file(path):
    with open(path, 'r') as file:
        content = file.read()

    return content