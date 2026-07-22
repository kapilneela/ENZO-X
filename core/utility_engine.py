class UtilityEngine:

    def score(

        self,

        goal_alignment=0,

        confidence=0,

        importance=0,

        cost=0

    ):

        utility = (

            goal_alignment * 0.40 +

            confidence * 0.30 +

            importance * 0.20 -

            cost * 0.10

        )

        return round(

            utility,

            2

        )

    def best(

        self,

        candidates

    ):


        if not candidates:

            return None

        for item in candidates:

            item["utility"] = self.score(

                item.get(
                    "goal_alignment",
                    0
                ),

                item.get(
                    "confidence",
                    0
                ),

                item.get(
                    "importance",
                    0
                ),

                item.get(
                    "cost",
                    0
                )

            )

        candidates.sort(

            key=lambda x: x["utility"],

            reverse=True

        )

        return candidates[0]