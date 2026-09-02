import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class AirtelNexusAiCustomerGrowthPlatformCrew:
    """ICICI Bank Credit Card Cross-Sell AI crew"""

    @agent
    def icici_customer_360_profiler(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_customer_360_profiler"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_ml_prediction_engine(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_ml_prediction_engine"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_autonomous_decision_engine(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_autonomous_decision_engine"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_omnichannel_campaign_orchestrator(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_omnichannel_campaign_orchestrator"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_portfolio_optimization_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_portfolio_optimization_analyst"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_executive_ai_copilot(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_executive_ai_copilot"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @agent
    def icici_continuous_learning_engine(self) -> Agent:
        return Agent(
            config=self.agents_config["icici_continuous_learning_engine"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gemini/gemini-3-flash-preview",
            ),
        )

    @task
    def build_customer_360_profiles(self) -> Task:
        return Task(
            config=self.tasks_config["build_customer_360_profiles"],
            markdown=False,
        )

    @task
    def run_ml_predictions(self) -> Task:
        return Task(
            config=self.tasks_config["run_ml_predictions"],
            markdown=False,
        )

    @task
    def generate_next_best_action_decisions(self) -> Task:
        return Task(
            config=self.tasks_config["generate_next_best_action_decisions"],
            markdown=False,
        )

    @task
    def simulate_omnichannel_campaign_execution(self) -> Task:
        return Task(
            config=self.tasks_config["simulate_omnichannel_campaign_execution"],
            markdown=False,
        )

    @task
    def optimize_portfolio_and_calculate_roi(self) -> Task:
        return Task(
            config=self.tasks_config["optimize_portfolio_and_calculate_roi"],
            markdown=False,
        )

    @task
    def generate_executive_intelligence_brief(self) -> Task:
        return Task(
            config=self.tasks_config["generate_executive_intelligence_brief"],
            markdown=False,
        )

    @task
    def run_continuous_learning_and_platform_improvement(self) -> Task:
        return Task(
            config=self.tasks_config["run_continuous_learning_and_platform_improvement"],
            markdown=False,
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ICICI Bank Credit Card Cross-Sell AI crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="gemini/gemini-3-flash-preview"),
        )
