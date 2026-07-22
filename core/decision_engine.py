from agents.planner_agent import Planner
from agents.knowledge_agent import KnowledgeAgent
from core.nlu import NLU

planner = Planner()
knowledge = KnowledgeAgent()
nlu = NLU()


class DecisionEngine:

    def think(self, user_input):

        analysis = nlu.analyze(user_input)

        intent = analysis.get("intent", "unknown")
        topic = analysis.get("topic")

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

                return knowledge.search(topic)

        return None