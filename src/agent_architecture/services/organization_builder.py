from agent_architecture.agents.models.Agent import Agent
from agent_architecture.agents.models.planning.ProjectPlan import ProjectPlan
from agent_architecture.agents.models.Team import Team
from agent_architecture.agents.models.Project import Project
class OrganizationBuilder:
    def __init__(self, project_plan: ProjectPlan):
        self.project_plan = project_plan
    def make_teams(self) -> list[Team]:
        teams = []
        try:
            for team_plan in self.project_plan.teams:
                agents = []
                for agent_plan in team_plan.agents:
                    agent = Agent(name = agent_plan.name, role = agent_plan.role, responsibilities = agent_plan.responsibilities, capabilities = agent_plan.capabilities, required_tools = agent_plan.required_tools)
                    agents.append(agent)
                team = Team(name = team_plan.name, members = agents)
                teams.append(team)
        except Exception as e:
            print(f"Error occurred while making teams: {e}")
        return teams
    def make_project(self) -> Project:
        project = Project(name = self.project_plan.name, description = self.project_plan.description, teams = self.make_teams())
        return project