import json
import random


def search(query):

    with open("data/knowledge.json","r") as f:
        data=json.load(f)

    query=query.lower().strip()

    for key,responses in data["knowledge"].items():

        key=key.lower()

        # Direct match
        if key in query:
            return random.choice(responses)

        # Word overlap match
        query_words=set(query.split())
        key_words=set(key.split())

        score=len(query_words.intersection(key_words))

        if score>0:
            return random.choice(responses)

    return None