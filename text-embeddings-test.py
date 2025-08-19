import global_ai_credential

from vertexai.language_models import TextEmbeddingModel

en_model = TextEmbeddingModel.from_pretrained("text-embedding-005")

embed_banana = en_model.get_embeddings(["banana"])

len(embed_banana[0].values)

type(embed_banana[0].values)

embed_banana = en_model.get_embeddings(["banana"])
e_b = embed_banana[0].values

embed_apple = en_model.get_embeddings(["apple"])
e_a = embed_apple[0].values

embed_cat = en_model.get_embeddings(["cat"])
e_c = embed_cat[0].values

import numpy as np

s1 = np.dot(e_b, e_a)
s2 = np.dot(e_b, e_c)
s3 = np.dot(e_a, e_c)

print(s1)
print(s2)
print(s3)

res = en_model.get_embeddings(["Bonjour"])
en = res[0].values

en

embed_combined = en_model.get_embeddings(["banana", "apple", "cat"])
embed_combined


mul_model = TextEmbeddingModel.from_pretrained("text-multilingual-embedding-002")
res1 = mul_model.get_embeddings(["Bonjour"])
mul = res1[0].values

len(mul)

np.dot(en, mul)