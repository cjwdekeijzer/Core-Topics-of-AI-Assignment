import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="ft:gpt-4o-mini-2024-07-18:my-jewellery:custommodel:AHtRWvGk",
    messages=[{"role": "user", "content": "I suffer migraines and headaches, and I've been having trouble falling asleep. My muscles have been trembling and twitching. I sometimes feel dizzy."}],
    temperature=0.25,
    max_tokens=512,
    top_p=0.3,
    frequency_penalty=0,
    presence_penalty=0,
    response_format={
      "type": "text"
    }
)

answer = response.choices[0].message.content
print(answer)

