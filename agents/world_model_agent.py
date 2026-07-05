class WorldModel:

    def __init__(self):

        self.world={

            "ai":[
                "machine learning",
                "deep learning",
                "neural network"
            ],

            "deep learning":[
                "transformers",
                "cnn",
                "rnn"
            ],

            "neurotech":[
                "eeg",
                "brain signals"
            ]
        }


    def related(self,topic):

        topic=topic.lower()

        if topic in self.world:

            return self.world[
                topic
            ]

        return []