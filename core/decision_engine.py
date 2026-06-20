from agents.planner_agent import Planner
from agents.knowledge_agent import search
from core.nlu import NLU


planner = Planner()
nlu = NLU()


class DecisionEngine:

    def think(self, user_input):

        analysis = nlu.analyze(user_input)

        intent = analysis["intent"]
        topic = analysis["topic"]


        if intent == "learn":

            return planner.create_plan(
                f"learn {topic}"
            )


        elif intent == "build":

            return planner.create_plan(
                f"build {topic}"
            )


        elif intent == "ask":

            if topic:
                return search(topic)


        return None