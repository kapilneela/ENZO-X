class Context:

    def __init__(self):
        self.current_topic=None

    def set_topic(self,topic):

        self.current_topic=topic

    def get_topic(self):

        return self.current_topic