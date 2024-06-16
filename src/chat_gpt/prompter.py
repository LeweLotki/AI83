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
        prompt_base = "Napisz krótki opis(dwa zdania) o czym jest poniższa piosenka. Zwróć uwagę na konkretne zabiegi stylistyczne i narrację: " 
        
        songs = session.query(TableSongs).all()
        matching_names = session.query(TableDescription.name).all()
        matching_names_set = {name[0] for name in matching_names}

        for song in songs:
        
            if song.name in matching_names_set:
                continue

            print(f'\n {song.name} \n')
            prompt = prompt_base + song.content
            response = self.chat_gpt.get_response(prompt)
            print(response)
            new_description = TableDescription(
                name=song.name,
                description=response,
                content=song.content
            )
            session.add(new_description)
            session.commit()




