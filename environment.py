
class Environment:
    def __init__(self, data_source):
        self.data_source = data_source

    def get_data(self, agent_id):
        # Simulate different data being provided to agents
        return self.data_source.get(agent_id, "default_data")
