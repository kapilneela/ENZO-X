import json
import os


class AttentionAgent:

    def __init__(self):

        self.file = "data/attention.json"

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    {},
                    f,
                    indent=4
                )

    # --------------------------

    def score(

        self,

        user_input,

        workspace,

        state

    ):

        scores = {}

        text = user_input.lower()

        # Current topic

        topic = workspace.get(
            "topic"
        )

        if topic:

            if topic.lower() in text:

                scores[
                    topic
                ] = 10

        # Current intent

        intent = workspace.get(
            "intent"
        )

        if intent:

            scores[
                intent
            ] = 8

        # Emotion

        emotion = workspace.get(
            "emotion"
        )

        if emotion:

            scores[
                emotion
            ] = 6

        # Brain state topic

        previous = state.dump().get(
            "current_topic"
        )

        if previous:

            scores[
                previous
            ] = scores.get(
                previous,
                0
            ) + 5

        return dict(

            sorted(

                scores.items(),

                key=lambda x:x[1],

                reverse=True

            )

        )

    # --------------------------

    def focus(

        self,

        user_input,

        workspace,

        state

    ):

        scores=self.score(

            user_input,

            workspace,

            state

        )

        if not scores:

            return []

        return list(
            scores.keys()
        )[:3]