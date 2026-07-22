import json
import os


class ThoughtAgent:

    def __init__(self):

        self.file = "data/thoughts.json"

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w"
            ) as f:

                json.dump(
                    [],
                    f,
                    indent=4
                )

    # ----------------------------

    def load(self):

        with open(
            self.file,
            "r"
        ) as f:

            return json.load(f)

    # ----------------------------

    def save(
        self,
        thoughts
    ):

        with open(
            self.file,
            "w"
        ) as f:

            json.dump(
                thoughts,
                f,
                indent=4
            )

    # ----------------------------

    def think(

        self,

        user_input,

        focus

    ):

        thoughts=[]

        thoughts.append(

            f"User asked: {user_input}"

        )

        for item in focus:

            thoughts.append(

                f"Focus -> {item}"

            )

        data=self.load()

        data.extend(

            thoughts
        )

        data=data[-50:]

        self.save(data)

        return thoughts


    # ----------------------------

    def recent(self):

        data=self.load()

        return data[-10:]