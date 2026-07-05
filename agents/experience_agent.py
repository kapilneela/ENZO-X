import json
import os
from datetime import datetime


FILE = "data/experiences.json"


class ExperienceAgent:

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

            # Safety check
            if not isinstance(data,list):

                self.reset()

                return []

            return data

        except:

            self.reset()

            return []


    def save(self,data):

        with open(FILE,"w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def remember_experience(self,user_input):

        text=user_input.lower()


        triggers=[

            "i learned",
            "i built",
            "i created",
            "i started"
        ]


        for trigger in triggers:

            if trigger in text:

                experiences=self.load()

                experiences.append({

                    "time":str(datetime.now()),

                    "event":text
                })

                self.save(experiences)

                return "Experience stored."


        return None


    def latest(self):

        experiences=self.load()

        if len(experiences)==0:

            return None

        return experiences[-1]["event"]