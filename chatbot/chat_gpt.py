from openai import OpenAI
from environs import Env
env = Env()
env.read_env()
OPENAI_SECRET_KEY = env.str("OPENAI_SECRET_KEY")

client = OpenAI(
    api_key=OPENAI_SECRET_KEY
)


def chat_completions(prompt, model="gpt-3.5-turbo", temperature=0.7):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    if prompt:
        messages.append(
            {"role": "user", "content": prompt}
        )
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )

    return response.choices[0].message.content
