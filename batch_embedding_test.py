import global_ai_credential

# In - GCS  gs://vertexai2025//generative-ai/embeddings/embeddings_input.jsonl
# out - GCS  gs://vertexai2025/out_embed

from vertexai.preview import language_models
input_uri = (
    "gs://vertexai2025/embeddings/embeddings_input.jsonl"
)
# Format: `"gs://your-bucket-unique-name/directory/` or `bq://project_name.llm_dataset`
output_uri = "gs://vertexai2025/out_embed"


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