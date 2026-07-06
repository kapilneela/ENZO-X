from agents.reflection2_agent import Reflection2Agent
from core.nlu import NLU
from core.workspace import Workspace
from core.brain_state import BrainState
from agents.research_agent import ResearchAgent
from agents.planner_agent import Planner
from agents.response_agent import ResponseAgent
from agents.reasoning_agent import ReasoningAgent
from agents.critic_agent import CriticAgent
from agents.session_agent import SessionAgent
from agents.decision_agent import DecisionAgent
from agents.tool_agent import ToolAgent
from agents.graph_agent import GraphAgent
from agents.world_model_agent import WorldModel
from agents.episodic_agent import EpisodicAgent
from agents.emotion_agent import EmotionAgent
from core.blackboard import Blackboard
from agents.goal_agent import GoalAgent
from agents.task_agent import TaskAgent
from core.executive import Executive
from agents.planner2_agent import Planner2Agent
from core.cognitive_cycle import CognitiveCycle
from agents.reflection2_agent import Reflection2Agent
from memory.semantic_memory import SemanticMemory
from agents.reflection_agent import ReflectionAgent




class Brain:

    def __init__(self):

        # Core
        self.nlu = NLU()
        self.workspace = Workspace()
        self.state = BrainState()

        # Memory 
        self.semantic = SemanticMemory()
        self.reflection2 = Reflection2Agent()
        self.cycle = CognitiveCycle(
                    self,interval=10
                )

        # Main agents
        self.research = ResearchAgent()
        self.planner = Planner()
        self.response = ResponseAgent()
        self.reasoning = ReasoningAgent()
        self.critic = CriticAgent()
        self.goal_agent = GoalAgent()
        self.task_agent = TaskAgent()
        self.reflection = ReflectionAgent()
        
        # Support systems
        self.session = SessionAgent()
        self.decision = DecisionAgent()
        self.tools = ToolAgent()

        # Agentic systems
        self.graph = GraphAgent()
        self.world = WorldModel()
        self.episode = EpisodicAgent()
        self.emotion = EmotionAgent()
        self.emotion = EmotionAgent()
        self.blackboard = Blackboard()
        self.planner2 = Planner2Agent()

        # Executive Controller
        self.executive = Executive(self)
        self.cycle = CognitiveCycle(self, interval=5)
        self.executive.register("planner", self.planner)
        self.executive.register("planner2", self.planner2)
        self.executive.register("research", self.research)
        self.executive.register("reasoning", self.reasoning)
        self.executive.register("critic", self.critic)
        self.executive.register("response", self.response)
        self.executive.register("emotion", self.emotion)
        self.executive.register("episode", self.episode)
        self.executive.register("task", self.task_agent)

        self.executive.register(
            "planner",
            self.planner
        )

        self.executive.register(
            "research",
            self.research
        )


        self.executive.register(
            "reasoning",
            self.reasoning
        )

        self.executive.register(
            "response",
            self.response
        )

        self.executive.register(
            "critic",
            self.critic
        )

        self.executive.register(
            "tools",
            self.tools
        )

        self.executive.register(
            "emotion",
            self.emotion
        )

        self.executive.register(
            "world",
            self.world
        )

        self.executive.register(
            "episode",
            self.episode
        )

        self.executive.subscribe(
            "goal.created",
            self._goal_created
        )

        self.executive.subscribe(
            "research.finished",
            self._research_finished
        )

        self.executive.subscribe(
            "response.generated",
            self._response_generated
        )
        self.executive.register(
            "planner2",
            self.planner2
        )

    def start(self):
        self.cycle.start()


    def stop(self):
        self.cycle.stop()

    def cognitive_step(self):

        goal = self.goal_agent.highest_priority()

        if goal:

            print(
            "[ENZO]",
            "Thinking about:",
            goal["name"]
        )




    def think(self, user_input):

        # =====================
        # Reset workspace
        # =====================

        self.workspace.clear()

        lower = user_input.lower().strip()

        # =====================
        # Analyze
        # =====================

        analysis = self.nlu.analyze(
            user_input
        )

        intent = analysis.get(
            "intent",
            "unknown"
        )

        topic = analysis.get(
            "topic",
            None
        )

        # =====================
        # Emotion
        # =====================

        emotion = self.emotion.detect(
            user_input
        )

        mood = emotion.get(
            "mood",
            "neutral"
        )

        self.workspace.set(
            "emotion",
            mood
        )

        self.blackboard.write(
            "intent",
            intent
        )

        self.blackboard.write(
            "topic",
            topic
        )

        self.blackboard.write(
            "emotion",
            mood
        )


        # =====================
        # Save episode
        # =====================

        self.episode.remember(
            user_input
        )

        # =====================
        # Workspace
        # =====================

        self.workspace.set(
            "intent",
            intent
        )

        self.workspace.set(
            "topic",
            topic
        )

        # =====================
        # Reasoning
        # =====================

        reasoning = self.reasoning.reason(
            analysis
        )

        confidence = reasoning.get(
            "confidence",
            50
        )

        thoughts = reasoning.get(
            "thoughts",
            []
        )

        self.state.update(
            "last_intent",
            intent
        )

        self.state.update(
            "current_topic",
            topic
        )

        self.state.update(
            "confidence",
            confidence
        )

        for thought in thoughts:

            self.state.add_thought(
                thought
            )

        # Decision

        action = self.decision.decide(
            analysis
        )

        self.workspace.set(
            "action",
            action
        )

        # Related topics

        if topic:

            related = self.world.related(
                topic
            )

            if related:

                self.workspace.set(
                    "related_topics",
                    related
                )

        # Tool usage

        result = None

        if "time" in lower:

            result = self.tools.run(
                "time_tool",
                None
            )

        elif "idea" in lower:

            result = self.tools.run(
                "random_tool",
                None
            )

        # Main logic

        if result is None:

            if intent == "greeting":

                result = "Hello Kapil! 👋"


            elif intent == "learn":

                result = self.planner.create_plan(
                    f"learn {topic}"
                )

                self.workspace.set(
                    "plan",
                    result
                )

                self.executive.publish(
                    "goal.created",
                    topic
                )

                self.executive.add_task(
                    f"Learn {topic}",
                    priority=8
                )   


            elif intent == "build":

                result = self.planner.create_plan(
                    f"build {topic}"
                )

                self.workspace.set(
                    "plan",
                    result
                )

                
                self.executive.publish(
                    "goal.created",
                    topic
                )

                self.executive.add_task(
                    f"Build {topic}",
                    priority=10
                )


            elif intent == "ask":

                result = self.research.gather(
                    topic
                )

                self.workspace.set(
                    "research",
                    result
                )

                self.executive.publish(
                    "research.finished",
                    topic
                )




            elif intent == "emotion":

                if mood == "happy":

                    result = (
                        "That energy can be used on your next project."
                    )

                elif mood == "sad":

                    result = (
                        "Small progress still matters."
                    )

                elif mood == "focused":

                    result = (
                        "You seem focused. Good time to build."
                    )

                else:

                    result = (
                        "I understand."
                    )


            elif intent == "recent":

                recent = self.episode.recent()

                if not recent:

                    result = (
                        "No recent activity found."
                    )

                else:

                    lines=[]

                    for i,item in enumerate(
                        recent,
                        1
                    ):

                        event = item.get(
                            "event",
                            "Unknown"
                        )

                        lines.append(
                            f"{i}. {event}"
                        )

                    result=(
                        "Recent activity:\n\n"
                        + "\n".join(lines)
                    )


            else:

                result = (
                    "I don't understand that yet."
                )

        # Critic

        review = self.critic.review(
            result
        )

        if review == "bad":

            result = (
                "Answer not found."
            )

        # Emotion styling

        result = str(result)

        if mood == "happy":

            result =  result

        elif mood == "sad":

            result =  result

        elif mood == "focused":

            result =  result

        # =====================
        # Final response
        # =====================

        final_response = self.response.generate(
            result
        )

        self.session.add(
            user_input,
            final_response
        )

        self.executive.publish(
            "response.generated",
            final_response
        )

        return final_response


    def show_workspace(self):

        return self.workspace.show()

    def show_state(self):

        return self.state.dump()
    
    def executive_status(self):

        return self.executive.status()

    def next_task(self):

        return self.executive.execute_next()

    def show_history(self):

        return self.session.summary()


    # Executive Events

    def _goal_created(
        self,
        data
    ):

        print(
        f"[Executive] Goal Created -> {data}"
        )


    def _research_finished(
    self,
    data
    ):

        print(
        f"[Executive] Research Finished"
    )


    def _response_generated(
    self,
    data
    ):

        pass