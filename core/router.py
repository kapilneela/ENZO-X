from agents.memory_agent import process
from agents.experience_agent import ExperienceAgent
from agents.reflection_agent import ReflectionAgent
from agents.goal_agent import GoalAgent
from agents.task_agent import TaskAgent
from agents.vector_memory_agent import VectorMemoryAgent
from core.plugin_manager import PluginManager
from core.brain import Brain


brain = Brain()

experience = ExperienceAgent()

reflection = ReflectionAgent()

goal = GoalAgent()

task = TaskAgent()

plugins = PluginManager()

vector = VectorMemoryAgent()


def route(user_input):

    text = user_input.lower().strip()

    # MEMORY SYSTEM

    memory_response = process(
        user_input
    )

    if memory_response:

        return memory_response


    # EXPERIENCE RECALL

    if text == "what did i do recently":

        recent = experience.latest()

        if recent:

            return (
                f"Recently you: {recent}"
            )

        return "No experiences found."

    # REFLECTION

    if text == "reflect":

        return reflection.reflect()

    # GOAL SYSTEM

    goal_response = goal.set_goal(
        user_input
    )

    if goal_response:

        return goal_response


    if text == "what should i do today":

        return goal.suggest_today()

    # TASK SYSTEM

    task_response = task.add_task(
        user_input
    )

    if task_response:

        return task_response


    if text == "show tasks":

        return task.show_tasks()


    # EXPERIENCE STORAGE

    experience_response = (
        experience.remember_experience(
            user_input
        )
    )

    if experience_response:

        return experience_response


    # VECTOR MEMORY / SEMANTIC MEMORY

    if "remember about" in text:

        query = (
            text.replace(
                "remember about",
                ""
            )
            .strip()
        )

        result = vector.recall(
            query
        )

        if result:

            return result

        return (
            "No related memories found."
        )


    # Store meaningful inputs
    if len(text.split()) > 4:

        vector.remember(
            user_input
        )

    #Plugins
    plugin_response = plugins.execute(
    user_input
    )

    if plugin_response:
        return plugin_response



    # MAIN BRAIN

    return brain.think(
        user_input
    )