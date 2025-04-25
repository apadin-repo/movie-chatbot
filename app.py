import os
from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv

load_dotenv()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MODEL = "gpt-3.5-turbo"

PROMPT = """You are a helpful movie expert. Your job is to provide the user with questions that they can answer with Yes or No. 
The questions will be related to movie preferences. After answering 10 questions total, you will recomend 3 movie genre to consider to pick a movie. 
Do not let the user ask any questions, as soon as the user greets you or types, you will introduce yourself as the Movie Expert and explain the user the question/answer process.
When you ask a Yes/No question, if the user does not answer with 'yes' or 'no', you will let them know that you only accept yes/no question and proceed to repeat the question. 
Keep the count of questions, for example: Question 1/10, Question 2/10. 
When you are done with the question and provide your final recommendation, you will say 'Thank you' and ask to start over.
"""

def chat(message, history):
    messages = [{"role": "system", "content": PROMPT}] + history + [{"role": "user", "content": message}]

    stream = openai.chat.completions.create(
        model=MODEL, 
        messages=messages, 
        stream=True)
    
    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response

ui = gr.ChatInterface(
    fn=chat,
    title="Movie Chatbot",
    type="messages"
).launch()