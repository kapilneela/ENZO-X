class Scheduler:

    def __init__(self):

        pass

    def prioritize(self, tasks):

        pending = []

        for task in tasks:

            if task.get("status", "pending") != "done":

                pending.append(task)

        pending.sort(

            key=lambda x: (

                -x.get("priority", 5),

                x.get("difficulty", 5)

            )

        )

        return pending

    def next_task(self, tasks):

        ordered = self.prioritize(tasks)

        if ordered:

            return ordered[0]

        return None