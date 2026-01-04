from .ConstitutionProcessor import ConstitutionProcessor
from .VectorStore import VectorStore
from .ConstitutionalReranker import ConstitutionalReranker
from .LLMHandler import LLMHandler

class ConstitutionalRAG:
    def __init__(self):
        self.processor = None
        self.vector_store = VectorStore()
        self.reranker = ConstitutionalReranker()
        self.llm = LLMHandler()
        self.initialized = False
    
    def initialize(self, docx_path="constitutionrf.docx"):
        if self.initialized:
            return
        
        self.processor = ConstitutionProcessor(docx_path)
        chunks = self.processor.process()
        self.vector_store.create_collection()
        self.vector_store.add_chunks(chunks)
        self.initialized = True
    
    def ask(self, query: str, n_search=10, top_k=3):
        if not self.initialized:
            self.initialize()

        search_results = self.vector_store.search(query, n_results=n_search)

        if not search_results.get('documents'):
            return {"answer": "Не найдено релевантных статей", "sources": []}
        
        results_list = []
        for i in range(len(search_results['documents'][0])):
            results_list.append({
                'text': search_results['documents'][0][i],
                'metadata': search_results['metadatas'][0][i],
                'score': 1 - search_results['distances'][0][i] if search_results['distances'] else 0
            })

        reranked_results = self.reranker.rerank(query, results_list)

        top_results = reranked_results[:top_k]
        answer_data = self.llm.get_answer(query, top_results)

        relevant_articles = []
        for result in top_results:
            relevant_articles.append({
                'article': result['metadata'].get('article_number', '?'),
                'clause': result['metadata'].get('clause'),
                'score': result.get('rerank_score', result.get('score', 0)),
                'preview': result['text'][:150] + '...' if len(result['text']) > 150 else result['text']
            })
        
        return {
            "answer": answer_data['answer'],
            "sources": answer_data['sources'],
            "relevant_articles": relevant_articles
        }

if __name__ == "__main__":
    rag = ConstitutionalRAG()
    rag.initialize()

    result = rag.ask("Какие права есть у человека?")
    print("Ответ:", result['answer'][:200], "...")
    print("Источники:", result['sources'])
