import os
import json

from .chat_gpt import ChatGPT

class Prompter():

    def __init__(self):

        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("No API key found.")

        model = 'gpt-4o'
        self.chat_gpt = ChatGPT(api_key=api_key, model=model)

    def get_descriptions(self):
        return



