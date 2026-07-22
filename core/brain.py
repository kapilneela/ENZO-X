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
from agents.attention_agent import AttentionAgent
from agents.thought_agent import ThoughtAgent
from agents.knowledge_agent import KnowledgeAgent
from agents.reasoning2_agent import Reasoning2Agent
from agents.tool_selector_agent import ToolSelectorAgent
from agents.curiosity_agent import CuriosityAgent
from agents.summary_agent import SummaryAgent
from agents.prediction_agent import PredictionAgent
from agents.personality_agent import PersonalityAgent
from agents.context_agent import ContextAgent
from agents.scheduler_agent import SchedulerAgent
from agents.self_improvement_agent import SelfImprovementAgent
from agents.action_agent import ActionAgent
from agents.simulation_agent import SimulationAgent
from agents.evolution_agent import EvolutionAgent
from agents.imagination_agent import ImaginationAgent
from agents.debate_agent import DebateAgent
from agents.reality_agent import RealityAgent
from agents.strategy_agent import StrategyAgent
from agents.dream_agent import DreamAgent
from agents.subconscious_agent import SubconsciousAgent
from agents.anomaly_agent import AnomalyAgent
from agents.mission_agent import MissionAgent
from agents.social_agent import SocialAgent
from agents.survival_agent import SurvivalAgent
from core.perception import Perception
from core.mind_state import MindState
from core.utility_engine import UtilityEngine
from core.workspace import Workspace
from core.event_bus import EventBus
from core.tool_registry import ToolRegistry
from core.cognitive_engine import CognitiveEngine
from agents.memory_agent import MemoryAgent
#from agents.vision_agent import VisionAgent

class Brain:

    def __init__(self):

        # Core
        self.nlu = NLU()
        self.workspace = Workspace()
        self.state = BrainState()
        self.perception = Perception()
        self.mind = MindState()
        self.utility = UtilityEngine()
        self.workspace = Workspace()
        self.events = EventBus()
        self.tools = ToolRegistry()
        self.cognitive = CognitiveEngine(self)

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
        self.attention = AttentionAgent()
        self.knowledge = KnowledgeAgent()
        self.tool_selector = ToolSelectorAgent()
        self.curiosity = CuriosityAgent()
        self.summary = SummaryAgent()
        self.predictor=PredictionAgent()
        self.personality=PersonalityAgent()
        self.context=ContextAgent()
        self.memory = MemoryAgent()
        
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
        self.thought = ThoughtAgent()
        self.reasoning2 = Reasoning2Agent()
        self.scheduler=SchedulerAgent()
        self.improver=SelfImprovementAgent()
        self.action=ActionAgent()
        self.simulator=SimulationAgent()
        self.evolution=EvolutionAgent()
        self.imagination=ImaginationAgent()
        self.dream=DreamAgent()
        self.subconscious=SubconsciousAgent()
        self.anomaly=AnomalyAgent()
        self.mission=MissionAgent()
        self.social=SocialAgent()
        self.survival=SurvivalAgent()
        self.debate=DebateAgent()
        self.reality=RealityAgent()
        self.strategy=StrategyAgent()
        
        # Vision
        #self.vision = VisionAgent()

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
        self.tools.register("planner", self.planner)
        self.tools.register("knowledge", self.knowledge)
        self.tools.register("reasoning", self.reasoning)
        self.tools.register("memory", self.memory)
        #self.tools.register("vision", self.vision)
       

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
        
        
        emotion = self.emotion.detect(
            user_input
        )

        mood = emotion.get(
            "mood",
            "neutral"
        )

        perception = self.perception.perceive(
            user_input,
            context=self.workspace.show(),
            emotion=mood

        )
        
       


        # Reset workspace

        self.workspace.reset()

        lower = user_input.lower().strip()

        # Analyze

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

        # Emotion

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

        # Save episode

        self.episode.remember(
            user_input
        )

        # Workspace

        self.workspace.set(
            "intent",
            intent
        )

        self.workspace.set(
            "topic",
            topic
        )

        # Attention Agent

        focus = self.attention.focus(
            user_input,
            self.workspace,
            self.state
        )

        self.workspace.set(
            "focus",
            focus
        )



         # Thoughts (CoT)

        thoughts = self.thought.think(
            user_input,
            focus
        )

        self.workspace.set(
            "internal_thoughts",
            thoughts
        )

        # Reasoning

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

            tool = self.tools.get("time_tool")
            if tool:
                result = tool.execute(None)

        elif "idea" in lower:

            tool = self.tools.get("random_tool")
            if tool:
                result = tool.execute(None)
            
        
         
        self.workspace.reset()

        self.workspace.set("user_input", user_input)

        analysis = self.nlu.analyze(user_input)

        self.workspace.set("intent", analysis["intent"])
        self.workspace.set("topic", analysis["topic"])

        self.cognitive.process(self.workspace)



        
        # Knowledge Graph

        if topic:

            self.knowledge.connect(
            topic,
            "related_to",
            intent
        )
            

        # R2 Reasoning 

        knowledge=[]

        if topic:

            knowledge=(
                self.knowledge.related(
                    topic
                )
            )

        reasoning_stream=(
            self.reasoning2.analyze(
                user_input,
                focus,
                knowledge
            )
        )

        self.workspace.set(
            "reasoning_stream",
            reasoning_stream
        )

        # Tool Selector

        selected=(
            self.tool_selector.choose(
                user_input
            )
        )

        self.workspace.set(
            "selected_tool",
            selected
        )


        # Curiosity 

        question=(
            self.curiosity.wonder(
                topic
            )
        )

        self.workspace.set(
            "curiosity",
            question
        )
        


        # Simulation

        if topic:

            futures=(
                self.simulator.run(
                topic
                )
            )

            self.workspace.set(
                "futures",
                futures
            )

            dream=(
                self.imagination.dream(
                    futures
                )
            )

            self.workspace.set(
                "dream",
                dream
            )

        
        


        # Summary

        all_thoughts=[]

        # Thought agent thoughts
        internal = self.workspace.get(
            "internal_thoughts"
        )

        if internal:
            all_thoughts.extend(
                internal
            )

        # Reasoning stream thoughts
        reasoning = self.workspace.get(
            "reasoning_stream"
        )

        if reasoning:
            all_thoughts.extend(
                reasoning
            )

        summary = self.summary.summarize(
            all_thoughts
        )

        self.workspace.set(
            "summary",
            summary
        )

        # Prediction & Context

        prediction=self.predictor.predict(
            intent,
            topic
        )

        self.workspace.set(
            "prediction",
            prediction
        )

        context=self.context.build(
            self.workspace
        )

        self.workspace.set(
            "context",
            context
        )


    # Action
        next_action=self.action.act(

            intent,
            topic
        )

        self.workspace.set(
            "next_action",
            next_action
        )

        improvements=self.improver.suggest(
            self.workspace
        )

        self.workspace.set(
            "improvements",
            improvements
        )

                # Debate & Reality

        if topic:

            debates=(
        self.debate.argue(
            topic
        )
    )

            self.workspace.set(

        "debates",

        debates
    )

            futures=(
                self.workspace.get(
                    "futures"
                )
            )

            selected=(
                self.strategy.choose(
                    futures
                )
            )

        self.workspace.set(
            "strategy",
            selected
        )

        if selected:

            reality= self.reality.verify(
                        selected

                )
            
            self.workspace.set(
                "reality",
                reality
            )

        dream=self.dream.generate(topic)
        self.workspace.set(
            "dream",
            dream
        )

        mission=self.mission.create(topic)
        self.workspace.set(
            "mission",
            mission
        )

        social=self.social.analyze(
            user_input
        )
        self.workspace.set(
            "social",
            social
        )

        anomaly=self.anomaly.check(
            self.workspace
        )
        self.workspace.set(
            "anomaly",
            anomaly
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

        
        # =====================
        # Final response
        # =====================

            result=self.personality.response_style(
            result,
            mood
        )

        final_response=self.response.generate(
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
    
    
        return self.workspace.get("response") \
            or self.workspace.get("decision") \
            or self.workspace.show()


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