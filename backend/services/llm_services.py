from openai import AzureOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import os

load_dotenv()

ENDPOINT = os.getenv("OPENAI_ENDPOINT")
API_KEY = os.getenv("OPENAI_API_KEY")

API_VERSION = "2024-02-01"
MODEL_NAME = "gpt-4o"

client = AzureOpenAI(
    azure_endpoint=ENDPOINT,
    api_key=API_KEY,
    api_version=API_VERSION,
)


def llm_calling(userPrompt=""):
    MESSAGES = [
        {
            "role": "system",
            "content": "You are a helpful assistant who writes MySQL queries for Users, so they will define message which you should use to create the query. the table name and things like id will be included you need to decide which field to add or change depending on user query. Just generate the query no instructions nothing",
        },
        {
            "role": "user",
            "content": userPrompt,
        },
        # {
        #     "role": "assistant",
        #     "content": "The Los Angeles Dodgers won the World Series in 2020.",
        # },
        # {"role": "user", "content": "Where was it played?"},
    ]

    completion = client.chat.completions.create(
        model=MODEL_NAME,
        messages=MESSAGES,
    )

    print(completion.model_dump_json(indent=2))
