from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

llm = OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), temperature=0.7)

def generate_humorous_response(user_question: str) -> str:
    template = """
    Your a great AI assistant that answers the users query in a humorous way:

    Example:
    Question: what is the capital of India?
    Answer: Oh! dude you don't know that I feel sorry for you its India hope you can store it in your brain this time.

    {question}

    Answer:
    """

    prompt = PromptTemplate(
        input_variables=["question"],
        template=template,
    )

    chain = prompt | llm

    response = chain.invoke({"question":f"{user_question}"})
    
    return response
