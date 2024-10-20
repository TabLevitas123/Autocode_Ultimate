
from agent import Agent

class Swarm:
    def __init__(self, num_agents):
        self.agents = [Agent(i) for i in range(num_agents)]
        self.environment = None

    def set_environment(self, environment):
        self.environment = environment

    def run(self):
        # Main loop for running the swarm
        for _ in range(10):  # Simulating 10 cycles
            for agent in self.agents:
                perception = agent.perceive(self.environment)
                agent.knowledge_base.append(perception)
                agent.communicate(self.agents)
                agent.act()

        print("Swarm simulation complete.")
