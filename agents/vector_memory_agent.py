import json
import os
import numpy as np

from sentence_transformers import SentenceTransformer

FILE = "data/vector_memory.json"


class VectorMemoryAgent:

    def __init__(self):

        self.model = SentenceTransformer(
            'all-MiniLM-L6-v2'
        )

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


    def cosine_similarity(
        self,
        a,
        b
    ):

        a=np.array(a)
        b=np.array(b)

        return np.dot(a,b) / (
            np.linalg.norm(a)
            *
            np.linalg.norm(b)
        )


    def remember(self,text):

        memory=self.load()

        embedding=self.model.encode(
            text
        ).tolist()

        memory.append({

            "text":text,
            "embedding":embedding
        })

        self.save(memory)

        return "Stored in vector memory."


    def recall(self, query):

        memory = self.load()

        if len(memory) == 0:
            return None


        query_embedding = self.model.encode(
            query
    )


        best_match = None
        best_score = -1


        for item in memory:

            score = self.cosine_similarity(
                query_embedding,
                item["embedding"]
        )

            if score > best_score:

                best_score = score
                best_match = item


    # Safety check
        if best_match is None:

            return None


        if best_score > 0.4:

            return (
                f"Related memory: "
                f"{best_match.get('text','Unknown memory')}"
        )


        return None