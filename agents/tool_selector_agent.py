class ToolSelectorAgent:

    def choose(self,text):

        text=text.lower()

        if any(x in text for x in [
            "calculate",
            "solve",
            "math"
        ]):
            return "math"

        elif any(x in text for x in [
            "latest",
            "news",
            "search"
        ]):
            return "web"

        elif any(x in text for x in [
            "remember",
            "know",
            "memory"
        ]):
            return "memory"

        elif any(x in text for x in [
            "build",
            "project"
        ]):
            return "planner"

        return "default"