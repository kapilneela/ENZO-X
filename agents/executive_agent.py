from core.scheduler import Scheduler


class ExecutiveAgent:

    def __init__(self):

        self.scheduler = Scheduler()

    def choose_next(self, goal):

        if not goal:

            return None

        tasks = goal.get("tasks", [])

        return self.scheduler.next_task(tasks)

    def summarize(self, goal):

        if not goal:

            return "No active goal."

        task = self.choose_next(goal)

        if not task:

            return "Everything is completed."

        return (
            f"Current Goal: {goal['name']}\n\n"
            f"Next Task: {task['task']}"
        )