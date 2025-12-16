from agents.coordinator import Coordinator
from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.memory_agent import MemoryAgent

def main():
    coordinator = Coordinator(
        ResearchAgent(),
        AnalysisAgent(),
        MemoryAgent()
    )

    print("Multi-Agent Chat System (type 'exit' to quit)\n")

    while True:
        query = input("User: ")
        if query.lower() == "exit":
            break

        response = coordinator.handle_query(query)
        print("System:", response)

if __name__ == "__main__":
    main()
