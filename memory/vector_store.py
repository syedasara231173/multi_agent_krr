from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self):
        self.texts = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def add(self, text):
        self.texts.append(text)
        self.vectors = self.vectorizer.fit_transform(self.texts)

    def search(self, query, top_k=1):
        if not self.texts:
            return []

        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.vectors)[0]

        best_idx = similarities.argmax()
        return [(self.texts[best_idx], similarities[best_idx])]
