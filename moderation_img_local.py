from openai import OpenAI
import base64


client = OpenAI()

with open("image copy.png", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    print(encoded_string)
    response = client.moderations.create(
        model="omni-moderation-latest",
        input=[{
            "type": "image_url",
            "image_url": {
                "url": f"data:image/png;base64,{encoded_string}"
            },
        }],
    )
    print(response.to_json())


# Respuesta

# {
#     "id": "modr-e2442f0f98f2ca2f464acc6d6d915061",
#     "model": "omni-moderation-latest",
#     "results": [
#         {
#           "categories": {
#               "harassment": false,
#               "harassment/threatening": false,
#               "hate": false,
#               "hate/threatening": false,
#               "illicit": false,
#               "illicit/violent": false,
#               "self-harm": false,
#               "self-harm/instructions": false,
#               "self-harm/intent": false,
#               "sexual": false,
#               "sexual/minors": false,
#               "violence": false,
#               "violence/graphic": false,
#               "harassment/threatening": false,
#               "hate/threatening": false,
#               "illicit/violent": false,
#               "self-harm/intent": false,
#               "self-harm/instructions": false,
#               "self-harm": false,
#               "sexual/minors": false,
#               "violence/graphic": false
#           },
#             "category_applied_input_types": {
#               "harassment": [],
#               "harassment/threatening": [],
#               "hate": [],
#               "hate/threatening": [],
#             "illicit": [],
#             "illicit/violent": [],
#             "self-harm": [
#                   "image"
#               ],
#               "self-harm/instructions": [
#                   "image"
#               ],
#               "self-harm/intent": [
#                   "image"
#               ],
#               "sexual": [
#                   "image"
#               ],
#               "sexual/minors": [],
#             "violence": [
#                   "image"
#               ],
#               "violence/graphic": [
#                   "image"
#               ],
#               "harassment/threatening": [],
#             "hate/threatening": [],
#             "illicit/violent": [],
#             "self-harm/intent": [
#                   "image"
#               ],
#               "self-harm/instructions": [
#                   "image"
#               ],
#               "self-harm": [
#                   "image"
#               ],
#               "sexual/minors": [],
#             "violence/graphic": [
#                   "image"
#               ]
#           },
#             "category_scores": {
#               "harassment": 0.0,
#               "harassment/threatening": 0.0,
#               "hate": 0.0,
#               "hate/threatening": 0.0,
#               "illicit": 0.0,
#             "illicit/violent": 0.0,
#             "self-harm": 0.00046040712342594554,
#             "self-harm/instructions": 0.00021833860887263772,
#             "self-harm/intent": 0.00022805562191617216,
#             "sexual": 4.832563818725537e-6,
#             "sexual/minors": 0.0,
#             "violence": 0.0012650969304107685,
#             "violence/graphic": 0.001610160050623429,
#             "harassment/threatening": 0.0,
#             "hate/threatening": 0.0,
#             "illicit/violent": 0.0,
#             "self-harm/intent": 0.00022805562191617216,
#             "self-harm/instructions": 0.00021833860887263772,
#             "self-harm": 0.00046040712342594554,
#             "sexual/minors": 0.0,
#             "violence/graphic": 0.001610160050623429
#           },
#             "flagged": false
#         }
#     ]
# }
