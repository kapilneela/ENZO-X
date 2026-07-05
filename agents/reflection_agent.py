from agents.experience_agent import ExperienceAgent


class ReflectionAgent:

    def __init__(self):

        self.experience = ExperienceAgent()


    def reflect(self):

        experiences = self.experience.load()

        if len(experiences) == 0:

            return "I don't have enough experiences yet."


        observations=[]

        ai_count=0
        neuro_count=0
        build_count=0


        for item in experiences:

            event=item["event"]

            observations.append(
                "- "+event
            )


            if "ai" in event:

                ai_count+=1


            if "neuro" in event:

                neuro_count+=1


            if "built" in event:

                build_count+=1


        summary=[]


        if ai_count>0:

            summary.append(
                f"You mentioned AI {ai_count} times."
            )


        if neuro_count>0:

            summary.append(
                f"You mentioned Neurotech {neuro_count} times."
            )


        if build_count>0:

            summary.append(
                f"You built {build_count} projects."
            )


        return f"""

Recent observations:

{chr(10).join(observations)}

Patterns noticed:

{chr(10).join(summary)}
"""