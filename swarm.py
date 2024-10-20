
from agent import Agent

class Swarm:
    def __init__(self, num_agents):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.environment = None

    def set_environment(self, environment):
        self.environment = environment

    def run(self):
        # Enhanced swarm behavior with coordination and conflict detection
        for cycle in range(10):  # Simulate multiple cycles
            print(f"Cycle {cycle+1}:")
            for agent in self.agents:
                perception = agent.perceive(self.environment)
                agent.knowledge_base.append(perception)
                agent.communicate(self.agents)
                agent.act()

        print("Swarm simulation complete with enhanced coordination.")
