import os
from dotenv import load_dotenv

import logging
logging.basicConfig(level=logging.INFO)

import groq

from utils import read_text_file

# Setting Constants
GROQ_API_KEY = os.getenv("GROQ_KEY", None)
MODEL = "llama-3.3-70b-versatile"

INSTRUCTION_PATH = os.path.join(os.path.dirname(__file__), r"prompts\sys_instruction.md")
INSTRUCTION_PROMPT = read_text_file(path=INSTRUCTION_PATH)


# Initialising Groq Client
if GROQ_API_KEY:
    client = groq.Groq(
        api_key=GROQ_API_KEY,
    )


def construct_prompt(resume_content, job_description):
    system_msg = {
        "role" : "system",
        "content" : INSTRUCTION_PROMPT
    }

    user_msg = {
        "role" : "user",
        "content" : f"""
            Resume Content :\n {resume_content}\n\n
            Job Description :\n {job_description}\n\n
        """
    }

    final_prompt = [system_msg, user_msg]
    return final_prompt



def invoke_llm(prompt):

    logging.info("Invoking LLM")
    logging.info(f"Model : {MODEL}")
    logging.debug(f"Prompt : {prompt}")

    response = client.chat.completions.create(
        messages= prompt,
        model= MODEL
    )

    response_content = response.choices[0].message.content
    logging.info("Response Received")
    logging.info(response_content)

    usage_metrics = response.usage
    logging.info(f"Completion Token - {usage_metrics.completion_tokens}")
    logging.info(f"Prompt Token - {usage_metrics.prompt_tokens}")
    logging.info(f"Total Tokens - {usage_metrics.total_tokens}")
    logging.info(f"Total Time - {usage_metrics.total_time}")


    return response_content


def get_match_score(resume_content, job_desc):
    prompt = construct_prompt(resume_content=resume_content,
                              job_description=job_desc)

    response = invoke_llm(prompt=prompt)
    print(response)
    return response



# --------- TESTING --------

if __name__ == "__main__":
    prompt = "What all are the basic concepts in RAG. Eg: vector, embedding etc. Explain in 5 short points."
    invoke_llm(prompt=prompt)
