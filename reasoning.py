from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="o1-mini",
    messages=[{
        "role": "user", "content": "Dame un ejemplo de como usar el modelo o1-mini de OpenAI para razonar sobre un texto."}]
)

print(response.choices[0].message.content)
print(response.usage)
