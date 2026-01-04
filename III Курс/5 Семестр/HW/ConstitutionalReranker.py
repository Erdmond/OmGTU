from sentence_transformers import SentenceTransformer
import numpy as np

class ConstitutionalReranker:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    
    def rerank(self, query: str, search_results: list) -> list:
        query_embedding = self.model.encode(query)
        
        for result in search_results:
            if 'embedding' not in result:
                result['embedding'] = self.model.encode(result['text'])

            similarity = np.dot(query_embedding, result['embedding']) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(result['embedding'])
            )
            result['rerank_score'] = float(similarity)

        search_results.sort(key=lambda x: x['rerank_score'], reverse=True)
        return search_results
