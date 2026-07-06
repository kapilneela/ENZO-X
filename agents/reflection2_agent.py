class Reflection2Agent:

    def __init__(self):

        self.history = []


    def reflect(

        self,

        event,

        success=True

    ):

        self.history.append(

            {

                "event": event,

                "success": success

            }

        )


    def latest(self):

        if not self.history:

            return None

        return self.history[-1]


    def failures(self):

        return [

            h

            for h in self.history

            if not h["success"]

        ]


    def improvements(self):

        ideas = []

        for item in self.failures():

            ideas.append(

                f"Improve: {item['event']}"

            )

        return ideas