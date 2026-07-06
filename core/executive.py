from collections import deque


class Executive:

    """
    ENZO Executive

    Responsibilities
    ----------------
    ✓ Event Bus
    ✓ Task Queue
    ✓ Blackboard Publishing
    ✓ Background Execution
    """

    def __init__(self, brain):

        self.brain = brain

        self.events = {}

        self.queue = deque()

        self.registry = {}

    # =====================================================
    # Agent Registry
    # =====================================================

    def register(self, name, agent):

        self.registry[name] = agent

    def get(self, name):

        return self.registry.get(name)

    # =====================================================
    # Event Bus
    # =====================================================

    def subscribe(self, event, callback):

        self.events.setdefault(event, []).append(callback)

    def publish(self, event, data=None):

        callbacks = self.events.get(event, [])

        for cb in callbacks:

            try:

                cb(data)

            except Exception as e:

                print("[Executive Event]", e)

    # =====================================================
    # Blackboard
    # =====================================================

    def publish_blackboard(self, outputs):

        if not hasattr(self.brain, "blackboard"):

            return

        if not isinstance(outputs, dict):

            return

        for key, value in outputs.items():

            self.brain.blackboard.write(

                key,

                value

            )

    # =====================================================
    # Queue
    # =====================================================

    def add_task(

        self,

        func,

        *args,

        **kwargs

    ):

        self.queue.append(

            (

                func,

                args,

                kwargs

            )

        )

    def execute_next(self):

        if not self.queue:

            return

        func, args, kwargs = self.queue.popleft()

        try:

            return func(

                *args,

                **kwargs

            )

        except Exception as e:

            print(

                "[Executive]",

                e

            )

    # =====================================================
    # Debug
    # =====================================================

    def status(self):

        return {

            "registered_agents": list(

                self.registry.keys()

            ),

            "queued_tasks": len(

                self.queue

            ),

            "events": list(

                self.events.keys()

            )

        }