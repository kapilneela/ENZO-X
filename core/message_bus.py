from collections import defaultdict


class MessageBus:

    def __init__(self):

        self.subscribers = defaultdict(list)

    def subscribe(
        self,
        event,
        callback
    ):

        self.subscribers[event].append(
            callback
        )

    def publish(
        self,
        event,
        data=None
    ):

        if event not in self.subscribers:
            return

        for callback in self.subscribers[event]:

            callback(data)

    def clear(self):

        self.subscribers.clear()