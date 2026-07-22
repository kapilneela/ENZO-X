class SocialAgent:

    def analyze(

        self,

        text

    ):

        text=text.lower()

        if "thanks" in text:

            return "positive"

        elif "bad" in text:

            return "negative"

        return "neutral"