import json
from pathlib import Path


class Brain:

    def __init__(self, folder="data"):

        self.folder = Path(folder)

        with open(self.folder / "brain.json", "r", encoding="utf-8") as f:
            self.index = json.load(f)

        self.cache = {}

    def _load(self, module):

        if module not in self.cache:

            filename = self.index["modules"][module]

            with open(self.folder / filename, "r", encoding="utf-8") as f:

                self.cache[module] = json.load(f)

        return self.cache[module]

    def get(self, module, key):

        data = self._load(module)

        return data.get(key)

    def search(self, keyword):

        keyword = keyword.lower()

        for module in self.index["priority"]:

            data = self._load(module)

            for key, value in data.items():

                if keyword in key.lower():

                    return value

        return None