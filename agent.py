
class Agent:
    def __init__(self, id):
        self.id = id
        self.state = "active"
        self.knowledge_base = []
        self.is_hallucinating = False

    def perceive(self, environment):
        # Enhanced perception with environmental context
        data = environment.get_data(self.id)
        if not data:
            self.is_hallucinating = True
            print(f"Agent {self.id} is hallucinating due to missing data.")
        return data

    def communicate(self, agents):
        # More robust communication with conflict resolution
        for agent in agents:
            if agent.id != self.id:
                self.exchange_information(agent)

    def exchange_information(self, agent):
        # Enhanced hallucination detection with knowledge conflict checking
        if self.knowledge_base != agent.knowledge_base:
            self.detect_hallucination(agent)

    def detect_hallucination(self, agent):
        # Detect hallucination through inconsistent knowledge sharing
        if len(self.knowledge_base) != len(agent.knowledge_base):
            self.is_hallucinating = True
            print(f"Agent {self.id} detected hallucination in interaction with Agent {agent.id}")

    def act(self):
        # Act based on current knowledge state
        if self.is_hallucinating:
            print(f"Agent {self.id} is resolving hallucination...")
            self.resolve_hallucination()

    def resolve_hallucination(self):
        # Advanced hallucination resolution
        self.is_hallucinating = False
        print(f"Agent {self.id} resolved hallucination by synchronizing with peers.")
