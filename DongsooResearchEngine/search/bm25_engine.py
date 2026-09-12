from rank_bm25 import BM25Okapi

class BM25Engine:

    def __init__(self):

        self.documents = []
        self.bm25 = None

    def build(self, documents):

        self.documents = documents

        tokenized = [
            doc.split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(
            tokenized
        )

    def search(
        self,
        query,
        top_k=10
    ):

        tokens = query.split()

        scores = self.bm25.get_scores(
            tokens
        )

        ranked = sorted(
            enumerate(scores),
            key=lambda x:x[1],
            reverse=True
        )

        return ranked[:top_k]