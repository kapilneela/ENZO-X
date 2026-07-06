import json
import os
from datetime import datetime

from agents.goal_agent import GoalAgent


class TaskAgent:

    def __init__(self):

        self.goal = GoalAgent()

        self.file = "data/tasks.json"

        os.makedirs("data", exist_ok=True)

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:

                json.dump([], f, indent=4)

        self.tasks = self.load()


    def load(self):

        try:

            with open(self.file, "r") as f:

                return json.load(f)

        except:

            return []


    def save(self):

        with open(self.file, "w") as f:

            json.dump(
                self.tasks,
                f,
                indent=4
            )


    def add(

        self,

        goal,

        title,

        priority=5,

        depends_on=None

    ):

        task = {

            "id": len(self.tasks)+1,

            "goal": goal,

            "title": title,

            "status": "todo",

            "priority": priority,

            "depends_on": depends_on,

            "created": str(datetime.now()),

            "completed": None

        }

        self.tasks.append(task)

        self.goal.add_task(
            goal,
            title
        )

        self.save()

        return task


    def start(self, title):

        for task in self.tasks:

            if task["title"].lower()==title.lower():

                task["status"]="in_progress"

                self.save()

                return True

        return False


    def complete(self, title):

        for task in self.tasks:

            if task["title"].lower()==title.lower():

                task["status"]="completed"

                task["completed"]=str(datetime.now())

                self.goal.finish_task(
                    task["goal"],
                    task["title"]
                )

                self.save()

                return True

        return False


    def block(self,title):

        for task in self.tasks:

            if task["title"].lower()==title.lower():

                task["status"]="blocked"

                self.save()

                return True

        return False


    def pending(self):

        return [

            t for t in self.tasks

            if t["status"]!="completed"

        ]


    def completed(self):

        return [

            t for t in self.tasks

            if t["status"]=="completed"

        ]


    def next_task(self):

        pending=self.pending()

        if not pending:

            return None

        pending=sorted(

            pending,

            key=lambda x:x["priority"],

            reverse=True

        )

        return pending[0]


    def goal_tasks(

        self,

        goal

    ):

        return [

            t for t in self.tasks

            if t["goal"].lower()==goal.lower()

        ]


    def remove(self,title):

        self.tasks=[

            t for t in self.tasks

            if t["title"].lower()!=title.lower()

        ]

        self.save()


    def show(self):

        return self.tasks