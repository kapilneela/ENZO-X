import json
import os
from datetime import datetime


class GoalAgent:

    def __init__(self):

        self.file = "memory/goals.json"

        os.makedirs("memory", exist_ok=True)

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump([], f, indent=4)

        self.goals = self.load()


    def load(self):

        try:

            with open(self.file, "r") as f:
                return json.load(f)

        except Exception:

            return []


    def save(self):

        with open(self.file, "w") as f:

            json.dump(
                self.goals,
                f,
                indent=4
            )


    def add(self, name):

        for goal in self.goals:

            if goal["name"].lower() == name.lower():

                return False

        self.goals.append({

            "id": len(self.goals) + 1,

            "name": name,

            "status": "active",

            "progress": 0,

            "priority": 5,

            "created": str(datetime.now()),

            "completed": None,

            "tasks": []

        })

        self.save()

        return True


    def remove(self, name):

        self.goals = [

            g for g in self.goals

            if g["name"].lower() != name.lower()

        ]

        self.save()


    def complete(self, name):

        for goal in self.goals:

            if goal["name"].lower() == name.lower():

                goal["status"] = "completed"

                goal["progress"] = 100

                goal["completed"] = str(datetime.now())

        self.save()


    def set_priority(

        self,

        name,

        priority

    ):

        for goal in self.goals:

            if goal["name"].lower() == name.lower():

                goal["priority"] = priority

                self.save()

                return True

        return False


    def update_progress(

        self,

        name,

        value

    ):

        value = max(0, min(100, value))

        for goal in self.goals:

            if goal["name"].lower() == name.lower():

                goal["progress"] = value

                self.save()

                return True

        return False


    def add_task(

        self,

        goal_name,

        task

    ):

        for goal in self.goals:

            if goal["name"].lower() == goal_name.lower():

                goal["tasks"].append({

                    "task": task,

                    "done": False

                })

                self.save()

                return True

        return False


    def finish_task(

        self,

        goal_name,

        task

    ):

        for goal in self.goals:

            if goal["name"].lower() == goal_name.lower():

                for t in goal["tasks"]:

                    if t["task"].lower() == task.lower():

                        t["done"] = True

                        self._recalculate(goal)

                        self.save()

                        return True

        return False


    def _recalculate(

        self,

        goal

    ):

        tasks = goal["tasks"]

        if not tasks:

            return

        completed = sum(

            1 for t in tasks

            if t["done"]

        )

        goal["progress"] = int(

            completed /

            len(tasks) *

            100

        )

        if goal["progress"] == 100:

            goal["status"] = "completed"

            goal["completed"] = str(datetime.now())


    def highest_priority(self):

        active = [

            g for g in self.goals

            if g["status"] == "active"

        ]

        if not active:

            return None

        return sorted(

            active,

            key=lambda x: x["priority"],

            reverse=True

        )[0]


    def active(self):

        return [

            g for g in self.goals

            if g["status"] == "active"

        ]


    def completed(self):

        return [

            g for g in self.goals

            if g["status"] == "completed"

        ]


    def get(

        self,

        name

    ):

        for goal in self.goals:

            if goal["name"].lower() == name.lower():

                return goal

        return None


    def show(self):

        return self.goals