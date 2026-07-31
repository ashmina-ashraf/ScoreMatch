from pathlib import Path
import os

from utils import read_text_file

DIRECTORY = Path(r"C:\Users\ashmi\OneDrive\Documents\GitHub\ScoreMatch\artifacts\job_descriptions")


def get_job_list():
    for file in DIRECTORY.glob("job*.txt"):
        yield file.name

def get_job_desc(filename):
    filepath = os.path.join(DIRECTORY, filename)

    content = read_text_file(path=filepath)
    return content