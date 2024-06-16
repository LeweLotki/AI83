from openai import OpenAI


class ChatGPT:
    def __init__(self, api_key: str, model="gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key)
        self.model = model

    def get_response(self, prompt: str) -> str:
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            model=self.model,
            max_tokens=300,
            temperature=0.7,
        )
        return chat_completion.choices[0].message.content.strip()
