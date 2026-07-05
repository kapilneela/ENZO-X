class Plugin:

    def run(self, text):

        text = text.lower()

        greetings = [

            "hi",
            "hello",
            "hey"
        ]


        if text in greetings:

            return (
                "Hello Kapil! 👋"
            )


        return None