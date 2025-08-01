from typing import TypedDict
from langgraph.graph import StateGraph, END
import os

# Define the state structure
class AgentState(TypedDict):
    input_value: int
    evaluation_result: str
    final_message: str

# Define nodes
def evaluate_number(state: AgentState) -> dict:
    threshold = 50
    input_value = state["input_value"]
    if input_value > threshold:
        return {"evaluation_result": "high"}
    else:
        return {"evaluation_result": "low"}

def handle_high_value(state: AgentState) -> dict:
    return {"final_message": f"The value {state['input_value']} is high!"}

def handle_low_value(state: AgentState) -> dict:
    return {"final_message": f"The value {state['input_value']} is low."}

# Define conditional edge function
def decide_path(state: AgentState) -> str:
    if state["evaluation_result"] == "high":
        return "high_handler"
    else:
        return "low_handler"

# Build the graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("evaluator", evaluate_number)
graph.add_node("high_handler", handle_high_value)
graph.add_node("low_handler", handle_low_value)

# Set entry point
graph.set_entry_point("evaluator")

# Add conditional edge
graph.add_conditional_edges(
    "evaluator",
    decide_path,
    {
        "high_handler": "high_handler",
        "low_handler": "low_handler"
    }
)

# Add edges to end
graph.add_edge("high_handler", END)
graph.add_edge("low_handler", END)

# Compile the graph
compiled_graph = graph.compile()

# Test the graph
result_high = compiled_graph.invoke({"input_value": 75})
result_low = compiled_graph.invoke({"input_value": 25})

print("High value result:", result_high)
print("Low value result:", result_low)

# Simple ASCII visualization (using basic characters)
print("\nGraph Structure:")
print("+-------------+")
print("|  evaluator  |")
print("+------+------+")
print("       |")
print("       +-----> high_handler -> END")
print("       |")
print("       +-----> low_handler -> END")

# Save graph structure to text file (using basic ASCII)
os.makedirs("visualizations", exist_ok=True)
with open("visualizations/graph_structure.txt", "w", encoding="utf-8") as f:
    f.write("Graph Structure:\n")
    f.write("+-------------+\n")
    f.write("|  evaluator  |\n")
    f.write("+------+------+\n")
    f.write("       |\n")
    f.write("       +-----> high_handler -> END\n")
    f.write("       |\n")
    f.write("       +-----> low_handler -> END\n")
    f.write("\nActual outputs:\n")
    f.write(f"High value result: {result_high}\n")
    f.write(f"Low value result: {result_low}\n")

print("\nGraph structure saved to visualizations/graph_structure.txt")