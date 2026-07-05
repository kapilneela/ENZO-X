import json
import os

FILE = "data/knowledge.json"


class LearningAgent:

    def __init__(self):

        if not os.path.exists(FILE):

            with open(FILE, "w") as f:
                json.dump({}, f)


    def load(self):

        try:

            with open(FILE, "r") as f:

                data = json.load(f)

            if not isinstance(data, dict):

                return {}

            return data

        except:

            return {}


    def save(self, data):

        with open(FILE, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def learn(self, text):

        text = text.strip()

        lower = text.lower()


        # Ignore questions
        blocked = [

            "what is",
            "who is",
            "where is",
            "why is",
            "how is",
            "tell me",
            "explain"
        ]


        for b in blocked:

            if lower.startswith(b):

                return None


        if " is " in lower:

            parts = text.split(
                " is ",
                1
            )

            if len(parts) == 2:

                key = parts[0].lower().strip()

                value = parts[1].strip()


                knowledge = self.load()

                knowledge[key] = value

                self.save(
                    knowledge
                )

                return (
                    f"Learned: {key}"
                )

        return None


    def recall(self, query):

        knowledge = self.load()

        query = query.lower()


        for key, value in knowledge.items():

            if key in query:

                return (
                    f"{key}: {value}"
                )

        return None