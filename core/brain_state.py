class BrainState:

    def __init__(self):

        self.state = {

            "current_topic": None,
            "last_intent": None,
            "confidence": 0,
            "thoughts": []
        }


    def update(self,key,value):

        self.state[key]=value


    def add_thought(self,thought):

        self.state["thoughts"].append(
            thought
        )


    def get(self,key):

        return self.state.get(
            key
        )


    def dump(self):

        return self.state