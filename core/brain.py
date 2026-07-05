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


class Brain:

    def __init__(self):

        # Core
        self.nlu = NLU()
        self.workspace = Workspace()
        self.state = BrainState()

        # Main agents
        self.research = ResearchAgent()
        self.planner = Planner()
        self.response = ResponseAgent()
        self.reasoning = ReasoningAgent()
        self.critic = CriticAgent()

        # Support systems
        self.session = SessionAgent()
        self.decision = DecisionAgent()
        self.tools = ToolAgent()

        # Agentic systems
        self.graph = GraphAgent()
        self.world = WorldModel()
        self.episode = EpisodicAgent()
        self.emotion = EmotionAgent()


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


            elif intent == "build":

                result = self.planner.create_plan(
                    f"build {topic}"
                )

                self.workspace.set(
                    "plan",
                    result
                )


            elif intent == "ask":

                result = self.research.gather(
                    topic
                )

                self.workspace.set(
                    "research",
                    result
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

        return final_response


    def show_workspace(self):

        return self.workspace.show()


    def show_state(self):

        return self.state.dump()


    def show_history(self):

        return self.session.summary()