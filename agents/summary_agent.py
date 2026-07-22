class SummaryAgent:

    def summarize(self, thoughts):

        if not thoughts:
            return "Nothing learned"

        # remove duplicates
        thoughts = list(
            dict.fromkeys(
                thoughts
            )
        )

        return " | ".join(
            thoughts[-5:]
        )