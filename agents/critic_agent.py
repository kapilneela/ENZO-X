class CriticAgent:

    def review(self, response):

        if response is None:

            return "bad"


        response = str(response).strip()


        # Too short or empty
        if len(response) < 2:

            return "bad"


        # Generic failure messages
        bad_patterns = [

            "i don't know",
            "i could not determine",
            "none"

        ]


        for pattern in bad_patterns:

            if pattern in response.lower():

                return "bad"


        return "good"