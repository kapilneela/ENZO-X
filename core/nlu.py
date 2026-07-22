class NLU:

    def analyze(self, text):

        text = text.lower().strip()

        words = text.split()

        intent = "unknown"
        topic = None

        # Greeting

        greetings = [
            "hi",
            "hello",
            "hey"
        ]

        # Exact word matching only
        if len(words) == 1 and words[0] in greetings:

            intent = "greeting"

        # Learn

        elif text.startswith("learn "):

            intent = "learn"

            topic = text.replace(
                "learn ",
                "",
                1
            ).strip()

        # Questions

        elif text.startswith("what is "):

            intent = "ask"

            topic = text.replace(
                "what is ",
                "",
                1
            ).strip()


        elif text.startswith("tell me about "):

            intent = "ask"

            topic = text.replace(
                "tell me about ",
                "",
                1
            ).strip()


        elif text.startswith("explain "):

            intent = "ask"

            topic = text.replace(
                "explain ",
                "",
                1
            ).strip()

        # Build

        elif text.startswith("build "):

            intent = "build"

            topic = text.replace(
                "build ",
                "",
                1
            ).strip()

        # Goal

        elif text.startswith("my goal is "):

            intent = "goal"

            topic = text.replace(
                "my goal is ",
                "",
                1
            ).strip()

        # Tasks

        elif text.startswith("add task "):

            intent = "task"

            topic = text.replace(
                "add task ",
                "",
                1
            ).strip()


        # Memory

        elif text.startswith("remember about "):

            intent = "memory"

            topic = text.replace(
                "remember about ",
                "",
                1
            ).strip()

        # Recent activity

        elif (
            "what i have done recently" in text
            or
            "what have i done recently" in text
            or
            "recent activity" in text
            or
            "what did i do recently" in text
        ):

            intent = "recent"
            topic = None

        # Emotion statements

        elif any(
            word in text
            for word in [
                "happy",
                "excited",
                "love",
                "sad",
                "tired",
                "angry",
                "upset"
            ]   
        ):

            intent = "emotion"
            topic = None

        return {
            "intent": intent,
            "topic": topic
        }