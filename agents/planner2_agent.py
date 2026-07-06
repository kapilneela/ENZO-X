class Planner2Agent:

    def __init__(self):

        self.templates = {

            "neuro ai": [

                "Study Neuroscience",

                "Learn EEG",

                "Learn Signal Processing",

                "Collect EEG Dataset",

                "Train Deep Learning Model",

                "Evaluate Accuracy",

                "Deploy"

            ],

            "machine learning": [

                "Python",

                "NumPy",

                "Pandas",

                "Matplotlib",

                "Statistics",

                "Scikit-Learn",

                "Projects"

            ],

            "web development": [

                "HTML",

                "CSS",

                "JavaScript",

                "React",

                "Backend",

                "Database",

                "Deployment"

            ]
        }

    def generate(self, goal):

        text = goal.lower()

        for key, tasks in self.templates.items():

            if key in text:

                return tasks.copy()

        return [

            "Research",

            "Planning",

            "Implementation",

            "Testing",

            "Deployment"

        ]