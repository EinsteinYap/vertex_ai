import global_ai_credential

from vertexai.language_models import TextEmbeddingModel , TextEmbeddingInput

model = TextEmbeddingModel.from_pretrained("text-embedding-005")

myin = TextEmbeddingInput("why sky is blue?" ,"QUESTION_ANSWERING")

myres = model.get_embeddings([myin])

fres = myres[0].values

myin = TextEmbeddingInput("why sky is blue?" ,"CLUSTERING")
myres1 = model.get_embeddings([myin])
fres1 = myres1[0].values


fres[:5]

fres1[:5]