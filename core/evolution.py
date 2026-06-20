import json
import os

HABIT_FILE="data/habits.json"


class Evolution:

    def __init__(self):

        if not os.path.exists(HABIT_FILE):

            with open(HABIT_FILE,"w") as f:
                json.dump({},f)


    def load(self):

        with open(HABIT_FILE,"r") as f:
            return json.load(f)


    def save(self,data):

        with open(HABIT_FILE,"w") as f:
            json.dump(data,f,indent=4)


    def learn(self,user_input):

        data=self.load()

        text=user_input.lower()

        if text not in data:

            data[text]=1

        else:

            data[text]+=1


        self.save(data)


    def check_dynamic(self,user_input):

        data=self.load()

        text=user_input.lower()


        for command,count in data.items():

            if count>=3 and text==command:

                return f"I noticed you frequently use: '{command}' ({count} times)"

        return None