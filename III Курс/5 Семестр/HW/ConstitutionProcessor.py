import re
from docx import Document
import json

class ConstitutionProcessor:
    def __init__(self, docx_path: str):
        self.docx_path = docx_path
    
    def load_document(self):
        doc = Document(self.docx_path)
        full_text = []
        for paragraph in doc.paragraphs:
            if paragraph.text.strip():
                full_text.append(paragraph.text)
        return '\n'.join(full_text)
    
    def extract_structure(self, text: str):
        lines = text.split('\n')
        articles = []
        current_article = None
        current_chapter = None
        current_section = None
        
        for line in lines:
            line = line.strip()
            
            if line.startswith('РАЗДЕЛ'):
                current_section = line
                continue
            
            if line.startswith('ГЛАВА'):
                current_chapter = line
                continue
            
            article_match = re.match(r'Статья\s+(\d+)', line)
            if article_match:
                if current_article:
                    articles.append(current_article)
                
                current_article = {
                    'article_number': article_match.group(1),
                    'text': '',
                    'clauses': [],
                    'chapter': current_chapter,
                    'section': current_section,
                    'full_title': line
                }
                continue
            
            if current_article and line:
                clause_match = re.match(r'(\d+)\.\s*(.+)', line)
                if clause_match:
                    clause_num = clause_match.group(1)
                    clause_text = clause_match.group(2)
                    current_article['clauses'].append({
                        'number': clause_num,
                        'text': clause_text
                    })
                else:
                    current_article['text'] += line + ' '
        
        if current_article:
            articles.append(current_article)
        
        return articles
    
    def create_chunks(self, articles):
        chunks = []
        chunk_id = 0
        
        for article in articles:
            title_chunk = {
                'id': chunk_id,
                'text': article['full_title'],
                'metadata': {
                    'article_number': article['article_number'],
                    'chapter': article['chapter'],
                    'section': article['section'],
                    'chunk_type': 'title'
                }
            }
            chunks.append(title_chunk)
            chunk_id += 1
            
            if article['text'].strip():
                main_chunk = {
                    'id': chunk_id,
                    'text': article['text'].strip(),
                    'metadata': {
                        'article_number': article['article_number'],
                        'chapter': article['chapter'],
                        'section': article['section'],
                        'chunk_type': 'main_text'
                    }
                }
                chunks.append(main_chunk)
                chunk_id += 1
            
            for clause in article['clauses']:
                clause_chunk = {
                    'id': chunk_id,
                    'text': f"{clause['number']}. {clause['text']}",
                    'metadata': {
                        'article_number': article['article_number'],
                        'chapter': article['chapter'],
                        'section': article['section'],
                        'chunk_type': 'clause',
                        'clause': clause['number']
                    }
                }
                chunks.append(clause_chunk)
                chunk_id += 1
        
        return chunks
    
    def process(self):
        text = self.load_document()
        articles = self.extract_structure(text)
        chunks = self.create_chunks(articles)
        return chunks
    
    def save_chunks(self, chunks, output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
    
    def load_chunks(self, input_path: str):
        with open(input_path, 'r', encoding='utf-8') as f:
            return json.load(f)
