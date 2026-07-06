class Executor:

    def execute(
        self,
        task
    ):

        if task is None:

            return None

        return {

            "status": "completed",

            "task": task["name"]

        }