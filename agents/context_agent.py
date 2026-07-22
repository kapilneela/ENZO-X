class ContextAgent:

    def build(

        self,

        workspace

    ):

        context=[]

        topic=workspace.get(
            "topic"
        )

        focus=workspace.get(
            "focus"
        )

        emotion=workspace.get(
            "emotion"
        )

        if topic:
            context.append(
                f"Topic={topic}"
            )

        if emotion:
            context.append(
                f"Mood={emotion}"
            )

        if focus:
            context.extend(
                focus
            )

        return context