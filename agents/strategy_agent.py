class StrategyAgent:

    def choose(

        self,

        futures

    ):

        if not futures:

            return None

        best=max(

            futures,

            key=lambda x:x["score"]

        )

        return {

            "selected":

            best["idea"],

            "score":

            best["score"]
        }