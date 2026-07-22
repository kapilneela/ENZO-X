class RealityAgent:

    def verify(self, idea):

        if idea is None:
            return {
                "realism": "Unknown",
                "reason": "No idea provided"
            }

        # Convert input into text

        if isinstance(idea, dict):

            text = str(

                idea.get("goal")
                or idea.get("topic")
                or idea.get("name")
                or idea

            ).lower()

        else:

            text = str(idea).lower()


        # Reality scoring

        if "teleport" in text:

            score = 20
            realism = "Low"

        elif "time travel" in text:

            score = 15
            realism = "Very Low"

        elif "immortality" in text:

            score = 10
            realism = "Very Low"

        elif "ai" in text:

            score = 75
            realism = "Medium"

        else:

            score = 95
            realism = "High"

        return {

            "realism": realism,

            "score": score,

            "text": text
        }