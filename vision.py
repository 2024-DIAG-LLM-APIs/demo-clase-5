from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un experto en análisis de imágenes. Responde en español. Dime en que se parecen las imagenes"},
        {"role": "user", "content": [
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://images.theconversation.com/files/547462/original/file-20230911-25-8o6sxn.jpg?ixlib=rb-4.1.0&rect=0%2C464%2C4252%2C2126&q=45&auto=format&w=1356&h=668&fit=crop"
                }
            },
            {"type": "image_url", "image_url": {
                "url": "https://media.es.wired.com/photos/6467c36ca566376ee967bc70/16:9/w_2560%2Cc_limit/To-Save-Downtowns-We-Must-Destroy-Them-Business-1252673490.jpg"
            }}
        ]
        }]
)

print(response.choices[0].message.content)
print(response.usage)
