class MindState:


    def __init__(self):

        self.reset()

    def reset(self):

        self.state = {

            "goal": None,

            "task": None,

            "focus": None,

            "emotion": "neutral",

            "strategy": None,

            "prediction": None,

            "confidence": 0,

            "thinking_mode": "normal",

            "reasoning_depth": 1,

            "attention": [],

            "last_action": None
        }

    def set(

        self,

        key,

        value

    ):

        self.state[key] = value

    def get(

        self,

        key,

        default=None

    ):

        return self.state.get(
            key,
            default
        )

    def update(

        self,

        **kwargs

    ):

        for k, v in kwargs.items():

            self.state[k] = v

    def snapshot(self):

        return dict(self.state)

    def __str__(self):

        lines = []

        for k, v in self.state.items():

            lines.append(
                f"{k}: {v}"
            )

        return "\n".join(lines)