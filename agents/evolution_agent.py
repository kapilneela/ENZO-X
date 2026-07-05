import json
import os

HABITS_FILE="data/habits.json"
COMMANDS_FILE="data/commands.json"


class EvolutionAgent:

    def __init__(self):

        if not os.path.exists(HABITS_FILE):

            with open(HABITS_FILE,"w") as f:
                json.dump({},f)

    def load_habits(self):

        with open(HABITS_FILE,"r") as f:
            return json.load(f)


    def save_habits(self,data):

        with open(HABITS_FILE,"w") as f:
            json.dump(data,f,indent=4)


    def load_commands(self):

        with open(COMMANDS_FILE,"r") as f:
            return json.load(f)


    def save_commands(self,data):

        with open(COMMANDS_FILE,"w") as f:
            json.dump(data,f,indent=4)


    def learn(self,user_input):

        text=user_input.lower().strip()

        data=self.load_habits()

        if text not in data:

            data[text]=1

        else:

            data[text]+=1

        self.save_habits(data)


    def generate_command(self):

        habits=self.load_habits()
        commands=self.load_commands()

        frequent=[]

        for action,count in habits.items():

            if count>=3:

                frequent.append(action)


        if len(frequent)>=3:

            new_command="smart mode"

            if new_command not in commands:

                commands[new_command]={

                    "actions":frequent[:3]
                }

                self.save_commands(commands)

                return f"Created new command: {new_command}"

        return None

