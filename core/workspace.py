from copy import deepcopy
from datetime import datetime


class Workspace:
    
    def __init__(self):

        self.reset()

    # ---------------------------------

    def reset(self):

        self.state = {

            "timestamp": str(datetime.now()),

            "user_input": None,

            "intent": None,

            "topic": None,

            "emotion": None,

            "focus": None,

            "vision": {},

            "audio": {},

            "knowledge": {},

            "memory": {},

            "reasoning": {},

            "plan": {},

            "decision": {},

            "actions": [],

            "response": None
        }

    # ---------------------------------

    def set(self, key, value):

        self.state[key] = value

    # ---------------------------------

    def update(self, key, value):

        if key not in self.state:

            self.state[key] = value

            return

        if isinstance(self.state[key], dict) and isinstance(value, dict):

            self.state[key].update(value)

        else:

            self.state[key] = value

    # ---------------------------------

    def get(self, key, default=None):

        return self.state.get(key, default)

    # ---------------------------------

    def append_action(self, action):

        self.state["actions"].append(action)

    # ---------------------------------

    def snapshot(self):

        return deepcopy(self.state)

    # ---------------------------------

    def clear_response(self):

        self.state["response"] = None

    # ---------------------------------

    def show(self):

        return self.state