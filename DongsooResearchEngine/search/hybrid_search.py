import numpy as np

class HybridSearch:

    def __init__(
        self,
        bm25,
        faiss
    ):

        self.bm25 = bm25
        self.faiss = faiss

    def search(
        self,
        query_embedding,
        query_text
    ):

        bm25_results = dict(
            self.bm25.search(
                query_text,
                top_k=30
            )
        )

        faiss_scores, faiss_ids = (
            self.faiss.search(
                query_embedding,
                top_k=30
            )
        )

        final_scores = {}

        for idx, score in bm25_results.items():

            final_scores[idx] = (
                final_scores.get(idx,0)
                + score
            )

        for idx, score in zip(
            faiss_ids,
            faiss_scores
        ):

            final_scores[idx] = (
                final_scores.get(idx,0)
                + float(score)*10
            )

        ranked = sorted(
            final_scores.items(),
            key=lambda x:x[1],
            reverse=True
        )

        return ranked[:10]