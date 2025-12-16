class ResearchAgent:
    def __init__(self):
        self.knowledge_base = {
            "neural networks": [
                "Feedforward Neural Networks",
                "Convolutional Neural Networks (CNNs)",
                "Recurrent Neural Networks (RNNs)",
                "Transformers"
            ],
            "transformer architectures": [
                "Self-attention enables parallelism",
                "High computational and memory cost",
                "Scales well with large datasets"
            ],
            "reinforcement learning": [
                "Policy-based methods",
                "Value-based methods",
                "Model-free and model-based learning",
                "Exploration vs exploitation challenge"
            ],
            "machine learning approaches": [
                "Supervised learning",
                "Unsupervised learning",
                "Reinforcement learning"
            ]
        }

    def research(self, topic: str):
        print(f"[ResearchAgent] Researching topic: {topic}")
        return self.knowledge_base.get(
            topic.lower(),
            ["No relevant information found."]
        )
