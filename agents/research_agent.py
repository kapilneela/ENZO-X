class ResearchAgent:

    def __init__(self):

        self.knowledge = {

            "ai":
            "Artificial Intelligence enables systems to learn, reason and make decisions.",

            "machine learning":
            "Machine Learning allows systems to learn patterns from data.",

            "python":
            "Python is a high-level programming language used for AI, web development, automation and data science.",

            "deep learning":
            "Deep Learning uses neural networks with multiple layers to learn complex patterns.",

            "neurotech":
            "Neurotechnology combines neuroscience and technology to interact with the brain."
        }


    def gather(self, topic):

        if topic is None:

            return (
                "I could not determine an appropriate response."
            )


        topic = topic.lower().strip()


        for key, value in self.knowledge.items():

            if key in topic:

                return value


        return (
            f"I don't know much about {topic} yet."
        )