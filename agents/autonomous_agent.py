class AutonomousAgent:
    """
    Decides what ENZO should focus on next.
    """

    def decide(self, goals, tasks):

        actions = []

        # -----------------------------
        # Active Goal
        # -----------------------------

        if goals:

            for goal in reversed(goals):

                if goal.get("status", "active") != "completed":

                    actions.append(
                        f"Continue goal: {goal['name']}"
                    )

                    break

        # -----------------------------
        # Next Task
        # -----------------------------

        pending = [

            task for task in tasks

            if task.get("status") != "completed"

        ]

        if pending:

            pending.sort(

                key=lambda x: x.get("priority", 0),

                reverse=True

            )

            task = pending[0]

            actions.append(

                f"Finish task: {task['title']}"

            )

        # -----------------------------
        # Response
        # -----------------------------

        if not actions:

            return "Nothing pending."

        output = "Today's focus:\n\n"

        for i, action in enumerate(actions, 1):

            output += f"{i}. {action}\n"

        return output