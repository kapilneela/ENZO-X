import random

class DreamAgent:

    def generate(self,topic):

        if not topic:
            return None

        dreams=[

            f"{topic} + autonomous AI",

            f"{topic} + brain interface",

            f"{topic} + robotics",

            f"{topic} + self-learning system"

        ]

        return random.choice(dreams)