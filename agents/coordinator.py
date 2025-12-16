import re

class Coordinator:
    def __init__(self, research_agent, analysis_agent, memory_agent):
        self.research_agent = research_agent
        self.analysis_agent = analysis_agent
        self.memory_agent = memory_agent

    def _is_complex(self, query: str) -> bool:
        keywords = ["analyze", "compare", "summarize", "trade-off", "recommend"]
        return any(k in query.lower() for k in keywords)

    def _extract_topic(self, query: str) -> str:
        query = query.lower()

        known_topics = [
            "neural networks",
            "transformer architectures",
            "reinforcement learning",
            "machine learning approaches"
        ]

        for topic in known_topics:
            if topic in query:
                return topic

        # Fallback: last two words
        words = query.split()
        return " ".join(words[-2:])

    def handle_query(self, query: str):
        print(f"\n[Coordinator] Query received: {query}")

        # Step 1: Check memory
        memory_hits = self.memory_agent.retrieve(query)
        if memory_hits:
            print("[Coordinator] Retrieved answer from memory.")
            return memory_hits[0][0]

        # Step 2: Decide execution plan
        if self._is_complex(query):
            print("[Coordinator] Complex query detected → Research + Analysis")

            topic = self._extract_topic(query)
            research_data = self.research_agent.research(topic)

            analysis_result = self.analysis_agent.analyze(
                research_data, query
            )

            # Store only meaningful knowledge
            if "Insufficient" not in analysis_result:
                self.memory_agent.store(
                    topic=topic,
                    content=analysis_result,
                    source="MockKnowledgeBase",
                    agent="AnalysisAgent",
                    confidence=0.9
                )

            return analysis_result

        else:
            print("[Coordinator] Simple query → Research only")

            topic = self._extract_topic(query)
            research_data = self.research_agent.research(topic)

            response = "\n".join(research_data)

            if "No relevant" not in response:
                self.memory_agent.store(
                    topic=topic,
                    content=response,
                    source="MockKnowledgeBase",
                    agent="ResearchAgent",
                    confidence=0.8
                )

            return response
