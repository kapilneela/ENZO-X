import json
import os


class KnowledgeAgent:

    def __init__(self):

        self.file = "data/knowledge_graph.json"

        if not os.path.exists(self.file):

            with open(self.file, "w") as f:

                json.dump({}, f, indent=4)

    # ----------------------------

    def load(self):

        with open(self.file, "r") as f:

            return json.load(f)

    # ----------------------------
    

    def save(self, data):

        with open(self.file, "w") as f:

            json.dump(
                data,
                f,
                indent=4
            )

    # ----------------------------

    def connect(

        self,

        source,

        relation,

        target

    ):

        graph = self.load()

        source = str(source).lower()
        target = str(target).lower()

        if source not in graph:

            graph[source] = []

        # Fix old/corrupted data
        if not isinstance(

            graph[source],

            list

        ):

            old = graph[source]

            graph[source] = []

            if old:

                graph[source].append({

                    "relation": "old",

                    "target": str(old)

                })

        connection = {

            "relation": relation,

            "target": target

        }

        # avoid duplicates
        if connection not in graph[source]:

            graph[source].append(

                connection

            )

        self.save(graph)

        return True

    # ----------------------------

    def related(

        self,

        topic

    ):

        graph = self.load()

        topic = topic.lower()

        if topic not in graph:

            return []

        if not isinstance(

            graph[topic],

            list

        ):

            return []

        return graph[topic]
    
    # Search 
    
    def search(self, query):
        """
        Search the knowledge graph.
        Returns:
        {
            "topic": "...",
            "connections": [...],
            "found": True/False
        }
        """

        graph = self.load()

        query = query.lower().strip()

    # Exact match
        if query in graph:

            data = graph[query]

            if not isinstance(data, list):
                data = []

                return {
                    "topic": query,
                    "connections": data,
                    "found": True
                }

    # Partial match
        for topic, relations in graph.items():

            if query in topic:

                if not isinstance(relations, list):
                    relations = []

                return {
                    "topic": topic,
                    "connections": relations,
                    "found": True
                }

        return {
            "topic": query,
            "connections": [],
            "found": False
        }