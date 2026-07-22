from core.memory import Memory

class MemoryAgent:

    def __init__(self):
        self.memory = Memory()

    def process(self, user_input):

        text = user_input.lower().strip()

        if "my name is" in text:

            name = text.split("my name is")[1].strip()

            self.memory.remember("username", name)

            return f"I'll remember your name as {name}"

        if "who am i" in text:

            name = self.memory.recall("username")

            if name:
                return f"You are {name}"

            return "I don't know yet."

        if text.startswith("remember"):

            try:
                statement = text.replace("remember", "").strip()

                key, value = statement.split(" is ", 1)

                self.memory.remember(
                    key.strip(),
                    value.strip()
                )

                return f"I'll remember that {key} is {value}"

            except:
                return "Use: remember X is Y"

        if text.startswith("what is my"):

            key = text.replace("what is my", "").strip()

            value = self.memory.recall(key)

            if value:
                return f"Your {key} is {value}"

        if text.startswith("what is"):

            key = text.replace("what is", "").strip()

            value = self.memory.recall(key)

            if value:
                return f"{key} is {value}"

        return None