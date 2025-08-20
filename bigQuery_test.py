import global_ai_credential

from vertexai.preview import language_models
input_uri = (
    "gs://vertexai2025/embeddings/embeddings_input.jsonl"
)
# output to Big query
output_uri = "bq://dependable-star-469404-k3.vertex_ds.indata"


textembedding_model = language_models.TextEmbeddingModel.from_pretrained(
    "text-embedding-005"
)

batch_prediction_job = textembedding_model.batch_predict(
    dataset=[input_uri],
    destination_uri_prefix=output_uri,
)
print(batch_prediction_job.display_name)
print(batch_prediction_job.resource_name)
print(batch_prediction_job.state)