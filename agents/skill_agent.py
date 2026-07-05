import json
import os

FILE="data/skills.json"

class SkillAgent:

    def load(self):

        try:
            with open(FILE,"r") as f:
                return json.load(f)
        except:
            return {}

    def save(self,data):

        with open(FILE,"w") as f:
            json.dump(data,f,indent=4)


    def update(self,topic):

        skills=self.load()

        skills[topic]=skills.get(
            topic,
            0
        )+1

        self.save(skills)

        return f"Skill updated: {topic}"


    def show(self):

        skills=self.load()

        if not skills:

            return "No skills tracked."


        result="Skills:\n\n"

        for k,v in skills.items():

            result+=(
                f"{k}: Lv {v}\n"
            )

        return result