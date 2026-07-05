import json
import os


FILE="data/graph.json"


class GraphAgent:

    def __init__(self):

        if not os.path.exists(FILE):

            with open(FILE,"w") as f:

                json.dump({},f)


    def load(self):

        with open(FILE,"r") as f:

            return json.load(f)


    def save(self,data):

        with open(FILE,"w") as f:

            json.dump(
                data,
                f,
                indent=4
            )


    def connect(
        self,
        node,
        relation,
        target
    ):

        graph=self.load()

        if node not in graph:

            graph[node]=[]


        graph[node].append({

            "relation":relation,
            "target":target
        })


        self.save(graph)


    def show(self):

        return self.load()