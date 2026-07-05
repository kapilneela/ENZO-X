class SessionAgent:

    def __init__(self):

        self.history = []


    def add(self, user, response):

        self.history.append({

            "user": user,
            "response": response

        })


    def latest(self, n=5):

        return self.history[-n:]


    def summary(self):

        if not self.history:

            return "No conversation history."


        output = "Recent conversation:\n\n"


        for item in self.history[-5:]:

            output += (
                f"You: {item['user']}\n"
            )

            output += (
                f"Enzo: {item['response']}\n\n"
            )


        return output