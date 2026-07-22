class ActionAgent:

    def act(

        self,

        intent,

        topic

    ):

        if intent=="build":

            return f"Prepare project structure for {topic}"

        elif intent=="learn":

            return f"Prepare learning roadmap for {topic}"

        elif intent=="ask":

            return f"Gather knowledge about {topic}"

        return "No action"