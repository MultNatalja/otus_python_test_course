import os


def get_pah(file_name):
    work_folder = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(work_folder, file_name)


CSV_FILE = get_pah('../../data/books.csv')
JSON_FILE = get_pah('../../data/users.json')

JSON_FILE_W = get_pah('../../data/result.json')
