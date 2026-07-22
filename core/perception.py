from datetime import datetime

from core.nlu import NLU


class Perception:

    def __init__(self):

        self.nlu = NLU()

    def perceive(

        self,

        user_input,
        text = None,
        image = None,
        context=None,

        emotion="neutral"

    ):
        

        analysis = self.nlu.analyze(
            user_input
        )

        perception = {

            "text": user_input,

            "intent": analysis.get(
                "intent",
                "unknown"
            ),

            "topic": analysis.get(
                "topic",
                None
            ),

            "entities": analysis.get(
                "entities",
                []
            ),

            "emotion": emotion,

            "confidence": analysis.get(
                "confidence",
                50
            ),

            "context": context or {},

            "timestamp": datetime.now(),

            "tokens": user_input.lower().split()
        }

        return perception