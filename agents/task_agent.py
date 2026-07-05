import json
import os

FILE = "data/tasks.json"


class TaskAgent:

    def __init__(self):

        if not os.path.exists(FILE):
            self.reset()


    def reset(self):

        with open(FILE,"w") as f:
            json.dump([],f,indent=4)


    def load(self):

        try:

            with open(FILE,"r") as f:
                data=json.load(f)

            if not isinstance(data,list):
                self.reset()
                return []

            return data

        except:
            self.reset()
            return []


    def save(self,data):

        with open(FILE,"w") as f:
            json.dump(data,f,indent=4)


    def add_task(self,user_input):

        text=user_input.lower()

        triggers=[

            "add task",
            "todo",
            "remember task"
        ]

        for trigger in triggers:

            if trigger in text:

                task=text.replace(
                    trigger,
                    ""
                ).strip()

                tasks=self.load()

                tasks.append({

                    "task":task,
                    "done":False
                })

                self.save(tasks)

                return f"Task added: {task}"

        return None


    def show_tasks(self):

        tasks=self.load()

        if len(tasks)==0:

            return "No tasks available."


        result="Tasks:\n\n"

        for i,item in enumerate(tasks,1):

            status="✓" if item["done"] else "○"

            result+=f"{i}. {status} {item['task']}\n"

        return result