from dataclasses import dataclass

@dataclass
class MemoryRecord:
    timestamp: str
    topic: str
    content: str
    source: str
    agent: str
    confidence: float
