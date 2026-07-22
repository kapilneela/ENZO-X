class PredictionAgent:

    def predict(

        self,

        intent,

        topic

    ):

        if intent=="learn":

            return (
                f"User may later build "
                f"{topic}"
            )

        elif intent=="build":

            return (
                f"User may ask for "
                f"implementation details"
            )

        elif intent=="ask":

            return (
                f"User may ask deeper questions"
            )

        return (
            "No prediction"
        )