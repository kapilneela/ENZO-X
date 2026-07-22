import json
import os
from datetime import datetime


class SchedulerAgent:

    def __init__(self):

        self.file="data/schedule.json"

        if not os.path.exists(self.file):

            with open(self.file,"w") as f:
                json.dump([],f,indent=4)

    def load(self):

        with open(self.file,"r") as f:
            return json.load(f)

    def save(self,data):

        with open(self.file,"w") as f:
            json.dump(data,f,indent=4)

    def add(

        self,
        action,
        trigger

    ):

        data=self.load()

        data.append({

            "action":action,
            "trigger":trigger,
            "created":str(datetime.now())

        })

        self.save(data)

        return "Scheduled"