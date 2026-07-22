import random


class SimulationAgent:

    def run(

        self,

        topic

    ):

        futures=[

            {
                "idea":
                f"{topic} as mobile app",

                "score":
                random.randint(
                    50,
                    80
                )
            },

            {
                "idea":
                f"{topic} with AI",

                "score":
                random.randint(
                    60,
                    100
                )
            },

            {
                "idea":
                f"{topic} as research project",

                "score":
                random.randint(
                    40,
                    90
                )
            }

        ]

        futures.sort(

            key=lambda x:x["score"],

            reverse=True
        )

        return futures