import importlib
import os


class ToolAgent:

    def __init__(self):

        self.tools={}

        self.load()


    def load(self):

        folder="tools"

        for file in os.listdir(folder):

            if file.endswith(".py"):

                name=file[:-3]

                module=importlib.import_module(
                    f"tools.{name}"
                )

                self.tools[name]=(
                    module.Tool()
                )


    def run(self,name,data):

        if name in self.tools:

            return self.tools[name].run(
                data
            )

        return None