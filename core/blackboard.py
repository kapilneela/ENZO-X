from threading import Lock


class Blackboard:

    def __init__(self):

        self.memory = {}

        self.lock = Lock()


    def write(

        self,

        key,

        value

    ):

        with self.lock:

            self.memory[key] = value


    def read(

        self,

        key,

        default=None

    ):

        with self.lock:

            return self.memory.get(

                key,

                default

            )


    def append(

        self,

        key,

        value

    ):

        with self.lock:

            if key not in self.memory:

                self.memory[key] = []

            self.memory[key].append(

                value

            )


    def remove(

        self,

        key

    ):

        with self.lock:

            if key in self.memory:

                del self.memory[key]


    def clear(self):

        with self.lock:

            self.memory.clear()


    def dump(self):

        with self.lock:

            return dict(self.memory)