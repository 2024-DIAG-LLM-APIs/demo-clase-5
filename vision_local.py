from openai import OpenAI
import base64


client = OpenAI()

with open("image copy.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(encoded_string)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{
            "role": "user",
            "content": [
                {"type": "image_url",
                 "image_url": {
                     "url": f"data:image/png;base64,{encoded_string}",
                     "detail": "low"
                 },
                 },
                {"type": "text", "text": "Dime que es lo que se ve en la imagen"}]
        }],
    )
    print(response.to_json())
