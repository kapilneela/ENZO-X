import json
import os
from datetime import datetime

FILE="data/episodes.json"


class EpisodicAgent:

    def __init__(self):

        if not os.path.exists(FILE):

            with open(FILE,"w") as f:

                json.dump([],f)


    def load(self):

        try:

            with open(FILE,"r") as f:

                data=json.load(f)

            if not isinstance(data,list):

                return []

            return data

        except:

            return []


    def save(self,data):

        with open(FILE,"w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def remember(self,event):

        ignored=[

            "hi",
            "hello",
            "hii",
            "hey"

        ]

        if event.lower().strip() in ignored:

            return


        data=self.load()

        data.append({

            "time":str(
                datetime.now()
            ),

            "event":event

        })

        self.save(data)


    def recent(self,n=5):

        data=self.load()

        cleaned=[]

        for item in data:

            if isinstance(item,dict):

                if "event" in item:

                    cleaned.append(item)

        return cleaned[-n:]