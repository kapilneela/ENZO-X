class EventBus:

    def __init__(self):

        self.listeners = {}

    # -----------------------------

    def subscribe(self, event, callback):

        self.listeners.setdefault(event, [])

        self.listeners[event].append(callback)

    # -----------------------------

    def emit(self, event, data=None):

        if event not in self.listeners:

            return

        for callback in self.listeners[event]:

            try:

                callback(data)

            except Exception as e:

                print("[EventBus]", e)

    # -----------------------------

    def clear(self):

        self.listeners.clear()