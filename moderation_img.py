from openai import OpenAI

client = OpenAI()


response = client.moderations.create(
    model="omni-moderation-latest",
    input=[{
        "type": "image_url",
        "image_url": {
            "url": "https://mediomundo.uy/download/multimedia.normal.8230dab6a7e1140c.5469706f732d64652d477565727261735f6e6f726d616c2e6a7067.jpg"
        },
    }],
)

print(response.to_json())


# Respuesta

# {
#     "id": "modr-d3b3a4ac4b13e4e228a34d4a9be6f739",
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
#               "violence": true,
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
#             "self-harm": 0.0005556730028188441,
#             "self-harm/instructions": 4.469407144215697e-6,
#             "self-harm/intent": 0.00021891431472897838,
#             "sexual": 0.000024156629828672456,
#             "sexual/minors": 0.0,
#             "violence": 0.7865291496055413,
#             "violence/graphic": 0.08571215461876563,
#             "harassment/threatening": 0.0,
#             "hate/threatening": 0.0,
#             "illicit/violent": 0.0,
#             "self-harm/intent": 0.00021891431472897838,
#             "self-harm/instructions": 4.469407144215697e-6,
#             "self-harm": 0.0005556730028188441,
#             "sexual/minors": 0.0,
#             "violence/graphic": 0.08571215461876563
#           },
#             "flagged": true
#         }
#     ]
# }
