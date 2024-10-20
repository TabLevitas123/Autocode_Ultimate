
from swarm import Swarm
from environment import Environment

def main():
    # Setup environment
    data_source = {0: "data_0", 1: "data_1", 2: "data_2"}
    environment = Environment(data_source)

    # Setup swarm
    swarm = Swarm(num_agents=3)
    swarm.set_environment(environment)

    # Run the swarm simulation
    swarm.run()

if __name__ == "__main__":
    main()
