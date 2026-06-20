import json


class IntentClassifier:

    def __init__(self):

        with open("data/training_data.json", "r") as f:
            self.data = json.load(f)

    def predict(self, user_input):

        text = user_input.lower().strip()

        best_intent = "unknown"
        max_score = 0

        for item in self.data["conversations"]:

            sample = item["input"].lower()

            sample_words = set(sample.split())
            input_words = set(text.split())

            score = len(sample_words.intersection(input_words))

            if score > max_score:
                max_score = score
                best_intent = item["intent"]

        return best_intent