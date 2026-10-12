
from agent_architecture.agents.models.DevStage import DevStage
from agent_architecture.agents.models.Agent import Agent
from agent_architecture.agents.models.Team import Team


class Project:
    def __init__(self, name, description, project_lead: Agent | None, teams: list[Team], current_stage: DevStage):
        self.name = name
        self.description = description
        self.project_lead = project_lead
        self.teams = teams