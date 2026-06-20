class NLU:

    def analyze(self, text):

        text = text.lower().strip()

        result = {
            "intent": "unknown",
            "topic": None
        }

        words = text.split()


        # Intent detection (ordered by priority)

        question_words = [
            "what",
            "define",
            "explain",
            "tell"
        ]

        learn_words = [
            "learn",
            "study",
            "master"
        ]

        build_words = [
            "build",
            "create",
            "make"
        ]


        # Ask intent first

        if any(word in words for word in question_words):

            result["intent"] = "ask"


        elif any(word in words for word in learn_words):

            result["intent"] = "learn"


        elif any(word in words for word in build_words):

            result["intent"] = "build"


        # Topic extraction

        topics = [

            "machine learning",
            "neurotech",
            "python",
            "ai"

        ]


        for topic in topics:

            if topic in text:

                result["topic"] = topic
                break


        return result