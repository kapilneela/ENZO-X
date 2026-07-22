class AnomalyAgent:

    def check(self,workspace):

        topic=workspace.get(
            "topic"
        )

        if not topic:

            return "Missing topic"

        if len(topic)>50:

            return "Topic unusually large"

        return None