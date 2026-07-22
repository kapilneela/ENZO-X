from pydoc import text

from core.brain import Brain

from agents.goal_agent import GoalAgent
from agents.task_agent import TaskAgent
from agents.experience_agent import ExperienceAgent
from agents.reflection_agent import ReflectionAgent
from agents.vector_memory_agent import VectorMemoryAgent
from agents.learning_agent import LearningAgent
from agents.skill_agent import SkillAgent
from agents.autonomous_agent import AutonomousAgent
from agents.web_agent import WebAgent
from core.thinking_loop import ThinkingLoop


class Enzo:

    def __init__(self):

        self.brain = Brain()
        
        self.brain.goal_agent
        self.brain.task_agent

        self.experience = ExperienceAgent()
        self.reflection = ReflectionAgent()
        self.vector = VectorMemoryAgent()
        self.learning = LearningAgent()

        self.skills = SkillAgent()
        self.auto = AutonomousAgent()
        self.web = WebAgent()

        self.loop = ThinkingLoop(
            self.brain,
            interval=5
        )

    def start(self):
        self.loop.start()
        self.brain.start()

    def stop(self):
        self.loop.stop()
        self.brain.stop()

    def think(self, user_input):

        text = user_input.lower().strip()

        # GOALS

        if text.startswith("goal "):

            goal = user_input[5:].strip()

            if self.brain.goal_agent.add(goal):
                return f"Goal added: {goal}"

            return "Goal already exists."

        if text in [
            "show goals",
            "show goal"
        ]:

            return self.brain.goal_agent.show()

        if text == "what should i do today":

            goal = self.brain.goal_agent.highest_priority()

            if goal:
                return (
                    f"Today's highest priority goal:\n\n"
                    f"{goal['name']}\n"
                    f"Progress: {goal['progress']}%"
                )

            return "No active goals."
        
        if text == "blackboard":

            return str(
                self.brain.blackboard.dump()
            )
            
        # TASKS

        if text.startswith("task "):

            try:

                data = user_input[5:]

                goal, task = data.split(":", 1)

                self.brain.task_agent.add(
                    goal.strip(),
                    task.strip()
                )

                return "Task added."

            except:

                return (
                    "Usage:\n"
                    "task Goal Name : Task Name"
                )

        if text in [
            "show task",
            "show tasks"
        ]:

            return self.brain.task_agent.show()


        # SKILLS

        if text.startswith("learn"):

            topic = text.replace(
                "learn",
                ""
            ).strip()

            self.skills.update(topic)

        if text == "show skills":

            return self.skills.show()
        
        # ATTENTION

        if text=="show focus":
            focus = self.brain.workspace.get(
                "focus"
            )

            if not focus:
                return "No focus available."

            return (
                "Current focus:\n\n"
                + "\n".join(
                f"- {x}"
                for x in focus
                )
            )
        
        # CoT

        if text=="show thoughts":

            thoughts=self.brain.thought.recent()
            return "\n".join(thoughts)


        # AUTONOMOUS

        if text in [
            "autonomous",
            "start autonomous mode"
        ]:

            return self.auto.decide(
                self.brain.goal_agent.show(),
                self.brain.task_agent.show()
            )

        # WEB
        
        if text.startswith("latest"):

            topic = text.replace(
                "latest",
                ""
            ).strip()

            return self.web.search(topic)

        # LEARNING MEMORY


        result = self.learning.recall(
            user_input
        )

        if result:
            return result

        result = self.learning.learn(
            user_input
        )

        if result:
            return result

        # VECTOR MEMORY

        if len(text.split()) > 4:

            self.vector.remember(
                user_input
            )

        if text.startswith("remember about"):

            query = text.replace(
                "remember about",
                ""
            ).strip()

            result = self.vector.recall(
                query
            )

            if result:
                return result
            


        # KNOWLEDGE GRAPH

        if text.startswith("connect"):

            parts=text.replace(
                "connect",
                "",
                1
            ).split(",")

            if len(parts)==3:

                return str(
            self.brain.knowledge.connect(
                parts[0].strip(),
                parts[1].strip(),
                parts[2].strip()
                )
            )


        if text.startswith("show graph"):
            topic=text.replace(
                "show graph",
                ""
            ).strip()

            result=self.brain.knowledge.related(
                topic
            )

            return str(result)
        
        #R2 REASONING

        if text=="show reasoning":

            data=self.brain.workspace.get(
                "reasoning_stream"
            )

            if not data:
                return "No reasoning available"

            return "\n".join(data)
        
        # T/C/S Functioning 

        if text=="show tool":

            return str(
                self.brain.workspace.get(
                    "selected_tool"
                )
            )


        if text=="show curiosity":

            return str(
                self.brain.workspace.get(
                    "curiosity"
                )
            )


        if text=="show summary":

            return str(
                self.brain.workspace.get(
                    "summary"
                )
            )
        
        # Prediction & Context

        if text=="show prediction":

            return str(
                self.brain.workspace.get(
                "prediction"
                )
            )


        if text=="show context":

            return str(
                self.brain.workspace.get(
                    "context"
                )
            )
        
        if text=="show action":

            return str(
            self.brain.workspace.get(
                "next_action"
            ))


        if text=="show improvements":

            return str(
                self.brain.workspace.get(
                "improvements"
            ))
            
        # DREAM 
        
        if text=="show dream":
            return str(
                self.brain.workspace.get(
                "dream"
                )
            )

        if text=="show mission":
            return str(
                self.brain.workspace.get(
                "mission"
                )
            )

        if text=="show anomaly":
            return str(
                self.brain.workspace.get(
                    "anomaly"
                )
            )

        if text=="show social":
            return str(
                self.brain.workspace.get(
                    "social"
                )
            )
        

        # SIMULATION

        if text=="show futures":

            return str(
                self.brain.workspace.get(
                    "futures"
                )
            )


        if text=="show dream":

            return str(
                self.brain.workspace.get(
                    "dream"
                )
            )
        
        # MIND STATE
        
        if text == "show mind":

            return str(
                self.brain.mind
            )

        if text == "show perception":
            return str(
                self.brain.perception.perceive(
                    user_input
                )
            )

        topic = None
        
        if text.startswith("what do you know about"):

            topic = text.replace(
                "what do you know about",
                "",
                1
            ).strip().lower()

        result = self.brain.semantic.recall(topic)

        if result:
            if topic:
                return f"{topic.title()} {result}"
            return result
        
        # BRAIN

        return self.brain.think(
            user_input
        )


        

        