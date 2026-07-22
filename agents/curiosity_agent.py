import random


class CuriosityAgent:

    def wonder(

        self,

        topic

    ):

        if not topic:
            return None

        questions=[

            f"How does {topic} work?",

            f"What can {topic} become?",

            f"What are applications of {topic}?",

            f"Can {topic} improve ENZO?"
        ]

        return random.choice(
            questions
        )