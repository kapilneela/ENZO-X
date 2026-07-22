import json
import os


class SemanticMemory:

    def __init__(

        self,

        path="data/semantic.json"

    ):

        self.path = path

        self.memory = {}

        self.load()


    def load(self):

        if os.path.exists(

            self.path

        ):

            with open(

                self.path,

                "r",

                encoding="utf-8"

            ) as f:

                self.memory = json.load(f)

        else:

            self.memory = {}


    def save(self):

        with open(

            self.path,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                self.memory,

                f,

                indent=4

            )


    def learn(

        self,

        key,

        value

    ):

        self.memory[key] = value

        self.save()


    def recall(

        self,

        key

    ):

        return self.memory.get(key)


    def all(self):

        return self.memory