import random


class Tool:

    def run(self,data):

        ideas=[

            "Build a neurotech app",
            "Study transformers",
            "Improve ENZO",
            "Create an AI project"

        ]

        return random.choice(
            ideas
        )