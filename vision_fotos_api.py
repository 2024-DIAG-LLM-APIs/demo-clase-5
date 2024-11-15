from openai import OpenAI
import requests


client = OpenAI()
response = requests.get("https://dog.ceo/api/breeds/image/random/3")


content = [{"type": "image_url", "image_url": {"url": url, "detail": "low"}}
           for url in response.json()['message']]
content.append(
    {"type": "text", "text": "Cuentame un chiste sobre las imagenes"})

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": content}],
    temperature=0.9
)

print(response.choices[0].message.content)
print(response.usage)
