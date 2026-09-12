class Retriever:

    def __init__(
        self,
        hybrid,
        docs,
        embedder
    ):

        self.hybrid = hybrid
        self.docs = docs
        self.embedder = embedder

    def retrieve(
        self,
        query,
        top_k=5
    ):

        q = self.embedder.encode(
            [query]
        )

        results = self.hybrid.search(
            q,
            query
        )

        return [
            self.docs[idx]
            for idx,_ in results[:top_k]
        ]