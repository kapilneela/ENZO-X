import json
import os

FILE = "data/goals.json"


class GoalAgent:

    def __init__(self):

        if not os.path.exists(FILE):
            self.reset()

    def reset(self):

        with open(FILE, "w") as f:
            json.dump([], f, indent=4)

    def load(self):

        try:

            with open(FILE, "r") as f:
                data = json.load(f)

            if not isinstance(data, list):
                self.reset()
                return []

            return data

        except Exception:
            self.reset()
            return []

    def save(self, data):

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

    def set_goal(self, user_input):

        text = user_input.lower()

        triggers = [
            "my goal is",
            "goal is",
            "i want to"
        ]

        for trigger in triggers:

            if trigger in text:

                goal = text.replace(
                    trigger,
                    ""
                ).strip()

                goals = self.load()

                goals.append(goal)

                self.save(goals)

                return f"Goal saved: {goal}"

        return None

    def suggest_today(self):

        goals = self.load()

        if len(goals) == 0:
            return "No goals found."

        latest = goals[-1]

        return f"""
Today's suggested actions:

1. Continue working on:
   {latest}

2. Study something related

3. Build a small improvement

4. Document progress
"""