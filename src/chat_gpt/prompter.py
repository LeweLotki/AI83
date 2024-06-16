import os

from .chat_gpt import ChatGPT

from models.songs import TableSongs
from models.description import TableDescription
from models import session

class Prompter():

    def __init__(self):

        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("No API key found.")

        model = 'gpt-4o'
        self.chat_gpt = ChatGPT(api_key=api_key, model=model)

    def get_descriptions(self):
        prompt = "Napisz krótki opis(dwa zdania) o czym jest poniższa piosenka: " 
        
        songs = session.query(TableSongs).all()
        for song in songs:
            
            prompt += song.content
            response = self.chat_gpt.get_response(prompt)
            print(response)

        return



