import chromadb
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = None
    
    def create_collection(self):
        try:
            self.collection = self.client.get_collection("constitution")
        except:
            self.collection = self.client.create_collection(
                name="constitution",
                metadata={"hnsw:space": "cosine"}
            )
    
    def embed_text(self, text):
        embedding = self.model.encode(text)
        return embedding.tolist()
    
    def add_chunks(self, chunks):
        if not self.collection:
            self.create_collection()
        
        ids = []
        embeddings = []
        documents = []
        metadatas = []
        
        for chunk in chunks:
            ids.append(str(chunk['id']))
            embeddings.append(self.embed_text(chunk['text']))
            documents.append(chunk['text'])
            metadatas.append(chunk['metadata'])
        
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas
        )
    
    def search(self, query, n_results=5):
        if not self.collection:
            self.create_collection()
        
        query_embedding = self.embed_text(query)
        
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        
        return results
