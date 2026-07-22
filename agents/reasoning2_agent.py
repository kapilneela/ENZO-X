class Reasoning2Agent:

    def __init__(self):

        pass

    def analyze(

        self,

        user_input,

        focus,

        knowledge

    ):

        thoughts=[]

        text=user_input.lower()

        # Intent reasoning

        if "what" in text:

            thoughts.append(
                "User wants information"
            )

        elif "build" in text:

            thoughts.append(
                "User wants creation"
            )

        elif "learn" in text:

            thoughts.append(
                "User wants learning"
            )

        # Attention reasoning

        for item in focus:

            thoughts.append(
                f"Attention on {item}"
            )

        # Knowledge graph reasoning

        for relation in knowledge:

            thoughts.append(
                f"{relation['target']} linked by "
                f"{relation['relation']}"
            )

        return thoughts