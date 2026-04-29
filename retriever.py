import faiss
import numpy as np

class Retriever:
    def __init__(self, embeddings, texts):
        self.texts = texts
        dim = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embeddings)

    def search(self, query_embedding, k=1):
        distances, indices = self.index.search(
            np.array([query_embedding]), k
        )
        return [self.texts[i] for i in indices[0]]