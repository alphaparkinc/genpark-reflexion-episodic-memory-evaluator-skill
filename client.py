"""Reflexion Episodic Memory Evaluator.
100% Python Standard Library.
"""

class ReflexionEpisodicEvaluator:
    """Reflexion verbal reinforcement learning architecture with episodic memory."""
    def __init__(self):
        self.memory = []

    def record_episode(self, trajectory, critique, score):
        self.memory.append({
            "trajectory": trajectory,
            "critique": critique,
            "score": score
        })

    def get_context_advice(self):
        if not self.memory:
            return "No previous episodic memories available."
        recent = self.memory[-1]
        return f"Reflected Wisdom: Previous attempt scored {recent['score']:.2f}. Critique: {recent['critique']}"
