class DecisionAgent:

    def decide(self,analysis):

        intent=analysis["intent"]

        if intent=="ask":

            return "research"

        elif intent=="learn":

            return "planner"

        elif intent=="build":

            return "planner"

        elif intent=="calculate":

            return "calculator"

        return "default"