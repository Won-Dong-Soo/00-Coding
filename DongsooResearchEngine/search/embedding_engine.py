from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL

class EmbeddingEngine:

    def __init__(self):

        self.model = SentenceTransformer(
            EMBEDDING_MODEL
        )

    def encode(self, texts):

        return self.model.encode(
            texts,
            show_progress_bar=True,
            normalize_embeddings=True
        )