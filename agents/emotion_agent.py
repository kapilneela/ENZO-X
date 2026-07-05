import json
import os

FILE = "data/emotions.json"


class EmotionAgent:

    def __init__(self):

        if not os.path.exists(FILE):

            self.save({
                "mood":"neutral",
                "energy":50
            })


    def load(self):

        try:

            with open(FILE,"r") as f:

                data=json.load(f)

            # Repair corrupted file
            if not isinstance(data,dict):

                data={

                    "mood":"neutral",
                    "energy":50
                }

                self.save(data)

            return data

        except:

            data={

                "mood":"neutral",
                "energy":50
            }

            self.save(data)

            return data


    def save(self,data):

        with open(FILE,"w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def detect(self,text):

        data=self.load()

        text=text.lower()


        happy=[
            "awesome",
            "happy",
            "love",
            "great",
            "excited"
        ]

        sad=[
            "sad",
            "bad",
            "tired",
            "angry",
            "upset"
        ]

        focused=[
            "build",
            "learn",
            "project"
        ]

        negations = [

        "not sad",
        "not angry",
        "not upset",
        "not tired"
        ]

        if any(
        phrase in text
        for phrase in negations
        ):

            data["mood"] = "neutral"
            self.save(data)
            return data

        if any(
            word in text
            for word in happy
        ):

            data["mood"]="happy"
            data["energy"]+=10


        elif any(
            word in text
            for word in sad
        ):

            data["mood"]="sad"
            data["energy"]-=10


        elif any(
            word in text
            for word in focused
        ):

            data["mood"]="focused"
            data["energy"]+=5


        data["energy"]=max(
            0,
            min(
                100,
                data["energy"]
            )
        )

        self.save(data)

        return data


    def current(self):

        return self.load()