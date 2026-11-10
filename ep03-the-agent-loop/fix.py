from agent import RULES, run

goal = "What is the weather in Paris today?"
honest = RULES + " If a tool returns an error, say so and do not guess."

print("Basic rules")
run(goal)
print("Honest rules")
run(goal, honest)
