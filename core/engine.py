from unittest import result

from matplotlib import text

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


class Enzo:

    def __init__(self):

        self.brain = Brain()

        self.goal = GoalAgent()
        self.task = TaskAgent()
        self.experience = ExperienceAgent()
        self.reflection = ReflectionAgent()
        self.vector = VectorMemoryAgent()
        self.learning = LearningAgent()

        self.skills = SkillAgent()
        self.auto = AutonomousAgent()
        self.web = WebAgent()


    def think(self,user_input):

        text=user_input.lower().strip()

        # Goals

        result=self.goal.set_goal(
            user_input
        )

        if result:
            return result


        if text=="what should i do today":

            return self.goal.suggest_today()

        # Tasks

        result=self.task.add_task(
            user_input
        )

        if result:
            return result


        if text in [
            "show task",
            "show tasks"
        ]:

            return self.task.show_tasks()


        # Skills

        if text.startswith("learn"):

            topic=text.replace(
                "learn",
                ""
            ).strip()

            self.skills.update(
                topic
            )


        if text=="show skills":

            return self.skills.show()

        # Autonomous

        if text in [
            "autonomous",
            "start autonomous mode"
        ]:

            goals=self.goal.load()
            tasks=self.task.load()

            return self.auto.decide(
                goals,
                tasks
            )

        # Web Intelligence

        if text.startswith(
            "latest"
        ):

            topic=text.replace(
                "latest",
                ""
            ).strip()

            return self.web.search(
                topic
            )

        # Learning Memory

        result=self.learning.recall(
            user_input
        )

        if result:
            return result


        result=self.learning.learn(
            user_input
        )

        if result:
            return result
        

        # Skills

        if text.startswith("learn"):

            topic = text.replace(
                "learn",
                ""
            ).strip()

            self.skills.update(
            topic
                )
            return self.brain.think(
                user_input
            )

        # Learning Memory 

        if not text.startswith("learn"):

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


        # Vector memory / Schematic Memory

        if len(text.split())>4:

            self.vector.remember(
                user_input
                )


        if "remember about" in text:

            query=text.replace(
                "remember about",
                ""
                )

            result=self.vector.recall(
                query
                )

            if result:
                return result


        return self.brain.think(
            user_input
            )