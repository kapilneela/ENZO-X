import json
import os


class PersonalityAgent:

    def __init__(self):

        self.file="data/personality.json"

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    {
                        "style":"jarvis"
                    },
                    f
                )

    def response_style(

        self,

        text,

        mood

    ):

        if mood=="focused":

            return (
                f"{text}"
            )

        elif mood=="happy":

            return (
                f"Nice. {text}"
            )

        elif mood=="sad":

            return (
                f"{text} Keep moving."
            )

        return text