
from agent_architecture.agents.models.Agent import Agent


class Team:
    def __init__(self, name: str, members: list[Agent], current_leader: Agent | None):
        self.name = name
        self.members = members
        self.current_leader = current_leader