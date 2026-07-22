class ToolAgent:

    def __init__(self):
        self.tools = {}

    def register(self, name, tool):
        self.tools[name] = tool

    def get(self, name):
        return self.tools.get(name)

    def exists(self, name):
        return name in self.tools

    def list(self):
        return list(self.tools.keys())

    def run(self, name, *args, **kwargs):

        tool = self.get(name)

        if tool is None:
            raise ValueError(f"Tool '{name}' not found.")

        # Function tool
        if callable(tool):
            return tool(*args, **kwargs)

        # Class with execute()
        if hasattr(tool, "execute"):
            return tool.execute(*args, **kwargs)

        # Class with run()
        if hasattr(tool, "run"):
            return tool.run(*args, **kwargs)

        raise TypeError(
            f"Tool '{name}' cannot be executed."
        )