from ConstitutionProcessor import ConstitutionProcessor
from VectorStore import VectorStore
import chromadb

print("1. Обработка документа...")
processor = ConstitutionProcessor("constitutionrf.docx")
chunks = processor.process()
print(f"   Создано {len(chunks)} чанков")

print("2. Создание векторной БД...")
store = VectorStore()
store.create_collection()
store.add_chunks(chunks)
print("   База данных готова!")

print("3. Проверка...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("constitution")
print(f"   В базе: {collection.count()} записей")
