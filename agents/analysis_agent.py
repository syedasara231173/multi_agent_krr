class AnalysisAgent:
    def analyze(self, data, query):
        print("[AnalysisAgent] Analyzing retrieved data")

        if not data or "No relevant" in data[0]:
            return "Insufficient data available for analysis."

        analysis = "Analysis Summary:\n"
        for item in data:
            analysis += f"- {item}\n"

        if "compare" in query.lower():
            analysis += "\nComparison indicates trade-offs in performance, scalability, and efficiency."

        if "recommend" in query.lower():
            analysis += "\nRecommendation: Choose based on data size, compute resources, and task complexity."

        return analysis
