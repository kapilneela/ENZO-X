class SubconsciousAgent:

    def detect(self,history):

        patterns=[]

        text=" ".join(history).lower()

        if "ai" in text:

            patterns.append(
                "User frequently discusses AI"
            )

        if "build" in text:

            patterns.append(
                "User likes creating projects"
            )

        return patterns