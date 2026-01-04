from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
from typing import Optional
from VectorStore import VectorStore
from ConstitutionalReranker import ConstitutionalReranker
from LLMHandler import LLMHandler

app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    n_results: Optional[int] = 5
    top_k: Optional[int] = 3

class QueryResponse(BaseModel):
    answer: str
    sources: list[str]
    relevant_articles: list[dict]

_vector_store = None
_reranker = None
_llm_handler = None

def get_components():
    global _vector_store, _reranker, _llm_handler
    
    if _vector_store is None:
        _vector_store = VectorStore()
        _vector_store.create_collection()
    
    if _reranker is None:
        _reranker = ConstitutionalReranker()
    
    if _llm_handler is None:
        
        _llm_handler = LLMHandler()
    
    return _vector_store, _reranker, _llm_handler

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        vector_store, reranker, llm = get_components()
        
        search_depth = max(request.top_k * 2, 10)
        search_results = vector_store.search(request.query, n_results=search_depth)
        
        if not search_results.get('documents'):
            raise HTTPException(status_code=404, detail="Не найдено релевантных статей")
        
        results_list = []
        for i in range(len(search_results['documents'][0])):
            results_list.append({
                'text': search_results['documents'][0][i],
                'metadata': search_results['metadatas'][0][i],
                'score': 1 - search_results['distances'][0][i] if search_results['distances'] else 0
            })
        
        reranked_results = reranker.rerank(request.query, results_list)
        
        top_results = reranked_results[:request.top_k]
        answer_data = llm.get_answer(request.query, top_results)
        
        relevant_articles = []
        for result in top_results:
            relevant_articles.append({
                'article': result['metadata'].get('article_number', '?'),
                'clause': result['metadata'].get('clause'),
                'score': result.get('rerank_score', result.get('score', 0)),
                'preview': result['text'][:150] + '...' if len(result['text']) > 150 else result['text']
            })
        
        return QueryResponse(
            answer=answer_data['answer'],
            sources=answer_data['sources'],
            relevant_articles=relevant_articles
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка: {str(e)}")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
