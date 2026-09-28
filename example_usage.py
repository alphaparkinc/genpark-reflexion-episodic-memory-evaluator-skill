from client import ReflexionEpisodicEvaluator

reflex = ReflexionEpisodicEvaluator()
reflex.record_episode(["Search DB", "Failed parse response"], "JSON missing required 'status' key", 0.3)

print("Episodic Memory Advice for next attempt:")
print(reflex.get_context_advice())
