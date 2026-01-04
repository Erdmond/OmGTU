import requests

class LLMHandler:
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.model = "qwen2.5:7b-instruct"
    
    def generate(self, prompt, max_tokens=500):
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0.1,
                        "max_tokens": max_tokens
                    }
                },
                timeout=30
            )
            return response.json().get("response", "") if response.status_code == 200 else ""
        except:
            return ""
    
    def format_context(self, results):
        context_parts = []
        for result in results:
            meta = result['metadata']
            text = f"Статья {meta.get('article_number', '?')}"
            if meta.get('clause'):
                text += f" пункт {meta['clause']}"
            text += f": {result['text'][:300]}"
            context_parts.append(text)
        return "\n".join(context_parts)
    
    def create_prompt(self, query, context):
        return f"""Ты — ассистент, который отвечает ТОЛЬКО на основе предоставленного контекста.
Если в контексте нет ответа - скажи "В предоставленных статьях Конституции нет информации об этом".

КОНТЕКСТ (статьи Конституции РФ):
{context}

ВОПРОС ПОЛЬЗОВАТЕЛЯ:
{query}

ПРАВИЛА:
1. Отвечай ТОЛЬКО на основе контекста выше
2. Если информации нет в контексте - не придумывай
3. Цитируй конкретные статьи (например: "Согласно статье 20...")
4. Не используй свои знания, только контекст

ОТВЕТ АССИСТЕНТА (на русском):"""
    
    def get_answer(self, query, search_results):
        context = self.format_context(search_results)
        prompt = self.create_prompt(query, context)
        answer = self.generate(prompt)
        return {
            "answer": answer,
            "sources": [
                f"Статья {r['metadata'].get('article_number', '?')}" 
                for r in search_results[:3]
            ]
        }
