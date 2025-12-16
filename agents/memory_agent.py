from memory.schema import MemoryRecord
from memory.vector_store import VectorStore
from datetime import datetime

class MemoryAgent:
    def __init__(self):
        self.records = []
        self.vector_store = VectorStore()

    def store(self, topic, content, source, agent, confidence):
        record = MemoryRecord(
            timestamp=str(datetime.now()),
            topic=topic,
            content=content,
            source=source,
            agent=agent,
            confidence=confidence
        )
        self.records.append(record)
        self.vector_store.add(content)
        print(f"[MemoryAgent] Stored memory on topic: {topic}")

    def retrieve(self, query):
        print("[MemoryAgent] Searching memory...")
        return self.vector_store.search(query)
