from resume_reader_utils import read_resume
import logging

logging.basicConfig(level=logging.INFO)

RESUME_PATH = r"C:\Users\ashmi\OneDrive\Documents\GitHub\ScoreMatch\Resume.pdf"

#Read Resume 
resume_content = read_resume(resume_path=RESUME_PATH)
logging.info("Fetched resume content.")
logging.debug(resume_content)

