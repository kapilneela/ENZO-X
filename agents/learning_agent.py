from memory.semantic_memory import SemanticMemory


class LearningAgent:

    def __init__(self):

        self.semantic = SemanticMemory()

    def learn(self, text):

        text = text.lower().strip()

        key = None
        value = None

        if text.startswith("remember"):

            statement = text.replace(
                "remember",
                "",
                1
            ).strip()

            if " is " in statement:

                key, value = statement.split(
                    " is ",
                    1
                )

                key = key.strip()
                value = "is " + value.strip()

        if key and value:

            self.semantic.learn(
                key,
                value
            )

            return f"Learned: {key}"

        return None


    def recall(self, text):

        text = text.lower()

        if text.startswith(
            "what do you know about"
        ):

            topic = text.replace(
                "what do you know about",
                "",
                1
            ).strip()

            result = self.semantic.recall(
                topic
            )

            if result:

                return (
                    f"{topic.title()} {result}"
                )

        return None