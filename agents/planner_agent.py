class Planner:

    def create_plan(self,text):

        text=text.lower()


        if "learn" in text:

            topic=text.replace("learn","").strip()

            return f"""
                Learning Plan for {topic}

                1. Understand basics
                2. Watch tutorials
                3. Practice examples
                4. Build mini projects
                5. Build advanced project
            """

        if "build" in text:

            project=text.replace("build","").strip()

            return f"""
                Project Plan for {project}

                1. Define features
                2. Create folder structure
                3. Build MVP
                4. Add advanced features
                5. Deploy
            """

        return None