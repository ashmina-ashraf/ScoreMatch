from resume_reader_utils import read_resume
from llm_utils import get_match_score
from job_list_utils import get_job_list, get_job_desc

import os

import logging
logging.basicConfig(level=logging.INFO)

RESUME_PATH = os.path.join(os.path.dirname(__file__), r"artifacts\Resume.pdf")
logging.info(f"Resume Path : {RESUME_PATH}")


#Read Resume 
resume_content = read_resume(resume_path=RESUME_PATH)
logging.info("Fetched resume content.")
logging.debug(resume_content)


job_lists = get_job_list()
for job in job_lists:
    logging.info(f"Fetching job description for {job}")

    job_desc = get_job_desc(job)
    logging.info("Fetch successful!")
    logging.debug(job_desc)

    logging.info("Getting Match Score ..")
    response = get_match_score(resume_content=resume_content,
                               job_desc=job_desc)