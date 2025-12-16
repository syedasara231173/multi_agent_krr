from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

def run_tests():
    coordinator = Coordinator(
        ResearchAgent(),
        AnalysisAgent(),
        MemoryAgent()
    )

    scenarios = [
        "What are the main types of neural networks?",
        "Research transformer architectures and analyze their efficiency",
        "What did we discuss about neural networks earlier?",
        "Find recent papers on reinforcement learning and analyze challenges",
        "Compare two machine learning approaches and recommend one"
    ]

    for q in scenarios:
        print("\nUSER:", q)
        print("SYSTEM:", coordinator.handle_query(q))

if __name__ == "__main__":
    run_tests()
