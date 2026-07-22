class CognitiveEngine:


    def __init__(

        self,

        brain

    ):

        self.brain = brain

    def process(

        self,

        workspace

    ):

        intent = workspace.get("intent")

        topic = workspace.get("topic")

        # Knowledge

        if topic:

            try:

                memory = self.brain.memory.search(topic)

                workspace.update(

                    "memory",

                    {

                        "related": memory

                    }

                )

            except Exception:

                pass

        # Planning
        
        if intent == "build":

            try:

                plan = self.brain.planner.create_plan(topic)

                workspace.set(

                    "plan",

                    plan

                )

            except Exception:

                pass

        # Decision

        if hasattr(

            self.brain,

            "decision_engine"

        ):

            decision = self.brain.decision_engine.think(

                workspace.get(

                    "user_input"

                )

            )

            workspace.set(

                "decision",

                decision

            )

        return workspace