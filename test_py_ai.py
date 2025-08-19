import global_ai_credential

from vertexai.generative_models import GenerativeModel
model = GenerativeModel("gemini-2.5-flash")

res = model.generate_content("What is capital of Malaysia?")

print(res.text)