import json


def execute(command):

    with open("data/commands.json","r") as f:

        data=json.load(f)

    command=command.lower()


    if command in data:

        actions=data[command]["actions"]

        result="\n".join(actions)

        return f"Executing:\n{result}"

    return None