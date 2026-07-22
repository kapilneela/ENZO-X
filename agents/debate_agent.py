class DebateAgent:

    def argue(

        self,

        topic

    ):

        if not topic:

            return []

        return [

            f"Why {topic} may succeed",

            f"Why {topic} may fail",

            f"What improves {topic}"

        ]