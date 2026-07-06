from collections import deque


class Scheduler:

    def __init__(self):

        self.queue = deque()

    def add(
        self,
        name,
        priority=5
    ):

        self.queue.append({

            "name": name,

            "priority": priority

        })

    def next(self):

        if not self.queue:

            return None

        tasks = sorted(

            self.queue,

            key=lambda x: x["priority"],

            reverse=True

        )

        task = tasks.pop(0)

        self.queue = deque(tasks)

        return task

    def show(self):

        return list(self.queue)