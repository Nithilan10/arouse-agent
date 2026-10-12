from pydantic import BaseModel, Field

from agent_architecture.agents.models.planning.AgentPlan import AgentPlan

class TeamPlan(BaseModel):
    name: str = Field(description="The name of the team")
    purpose: str = Field(description="The purpose of the team in the project, why is the team necessary?")
    responsibilities: list[str] = Field(description="The responsibilities of the team in the project")
    capabilities: list[str] = Field(description="The capabilities of the team in the project")
    required_tools: list[str] = Field(description="The tools required for the team to perform their role")
    agents: list[AgentPlan] = Field(description="The agents involved in the project")