import faiss
import numpy as np

from config import FAISS_PATH

class FaissEngine:

    def __init__(self):

        self.index = None

    def build(self, embeddings):

        dim = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(
            dim
        )

        self.index.add(
            embeddings.astype(
                np.float32
            )
        )

        faiss.write_index(
            self.index,
            str(FAISS_PATH)
        )

    def load(self):

        self.index = faiss.read_index(
            str(FAISS_PATH)
        )

    def search(
        self,
        query_embedding,
        top_k=10
    ):

        scores, ids = self.index.search(
            query_embedding.astype(
                np.float32
            ),
            top_k
        )

        return scores[0], ids[0]