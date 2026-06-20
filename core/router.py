from agents.memory_agent import process
from core.decision_engine import DecisionEngine

brain = DecisionEngine()


def route(user_input):

    # Memory system first
    memory_response = process(user_input)

    if memory_response:
        return memory_response


    # Main brain pipeline
    response = brain.think(user_input)

    if response:
        return response


    # Fallback
    return "I don't understand that yet."