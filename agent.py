
class Agent:
    def __init__(self, id):
        self.id = id
        self.state = "active"
        self.knowledge_base = []
        self.is_hallucinating = False

    def perceive(self, environment):
        # Perception logic to interact with the environment and other agents
        return environment.get_data(self.id)

    def communicate(self, agents):
        # Communication logic with other agents
        for agent in agents:
            if agent.id != self.id:
                self.exchange_information(agent)

    def exchange_information(self, agent):
        # Share knowledge with other agents and detect inconsistencies
        if self.knowledge_base != agent.knowledge_base:
            self.detect_hallucination(agent)

    def detect_hallucination(self, agent):
        # Basic hallucination detection: check for conflicting knowledge
        if len(self.knowledge_base) != len(agent.knowledge_base):
            self.is_hallucinating = True
            print(f"Agent {self.id} detected hallucination with Agent {agent.id}")

    def act(self):
        # Agent takes action based on its current state
        if self.is_hallucinating:
            print(f"Agent {self.id} is resolving hallucination...")
            self.resolve_hallucination()

    def resolve_hallucination(self):
        # Logic for resolving hallucination
        self.is_hallucinating = False
        print(f"Agent {self.id} resolved hallucination.")
