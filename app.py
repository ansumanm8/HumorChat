from fastapi import FastAPI
import schemas
from humorchatbot import generate_humorous_response
import uvicorn

""" API Integration implementation """

app = FastAPI()

@app.get('/')
def home():
    return {"greetings":"Welcome to HumorChat. add '/docs' at the end of the URL to get to the API Swagger"}

@app.post('/generate_humor_response')
def response_from_llm(request: schemas.CHAT):
    response = generate_humorous_response(request.question)
    return {
        "User": request.question,
        "humorous_guy😎": response.strip()
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="debug")
