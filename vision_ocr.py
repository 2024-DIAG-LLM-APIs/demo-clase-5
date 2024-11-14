from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Eres un experto en OCR. Responde en español. Respondeme preguntas sobre el texto de la imagen. Siempre responde en formato JSON. Extrae todos los datos posibles de la imagen."},
        {"role": "user", "content": [
            {"type": "image_url", "image_url": {
                "url": "https://lh7-us.googleusercontent.com/docsz/AD_4nXdVS8vUFlVk2gSUNSeM_G2pyTpD4HSn0-6zHbjFTszVVufF_JiYmqwH5uRdUHj4odqZTv-KQzzVzX4Rj5Q9HJq25N0Cv1PB-SDtDVQyGtN6eXibiBBYRlMq5M535OfuTIBsplDWqqFknZO1kiJbosRdNibA?key=jW9fTMfHotxUhADapVKVuw",
                "detail": "low"
            }}
        ]
        }],
    response_format={"type": "json_object"}
)

print(response.choices[0].message.content)
print(response.usage)
