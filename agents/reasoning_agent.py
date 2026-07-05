class ReasoningAgent:

    def reason(self,analysis):

        thoughts=[]

        intent=analysis["intent"]
        topic=analysis["topic"]


        thoughts.append(
            f"Detected intent: {intent}"
        )

        thoughts.append(
            f"Detected topic: {topic}"
        )


        confidence=0


        if intent!="unknown":
            confidence+=50

        if topic:
            confidence+=50


        return {

            "thoughts":thoughts,
            "confidence":confidence
        }