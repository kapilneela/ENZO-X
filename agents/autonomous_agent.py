class AutonomousAgent:

    def decide(
        self,
        goals,
        tasks
    ):

        actions=[]


        if goals:

            actions.append(
                f"Continue goal: {goals[-1]}"
            )


        for task in tasks:

            if not task["done"]:

                actions.append(
                    f"Finish task: {task['task']}"
                )

                break


        if not actions:

            return "Nothing pending."


        output="Today's focus:\n\n"

        for i,a in enumerate(
            actions,
            1
        ):

            output+=(
                f"{i}. {a}\n"
            )

        return output