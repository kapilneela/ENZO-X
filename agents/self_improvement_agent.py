import json
import os


class SelfImprovementAgent:

    def __init__(self):

        self.file="data/improvements.json"

        if not os.path.exists(self.file):

            with open(self.file,"w") as f:

                json.dump([],f)

    def suggest(

        self,

        workspace

    ):

        suggestions=[]

        if not workspace.get(
            "topic"
        ):

            suggestions.append(
                "Improve topic extraction"
            )

        if not workspace.get(
            "focus"
        ):

            suggestions.append(
                "Improve attention"
            )

        return suggestions