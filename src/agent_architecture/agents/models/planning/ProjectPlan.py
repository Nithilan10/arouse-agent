from pydantic import BaseModel, Field
from agent_architecture.agents.models.planning.TeamPlan import TeamPlan

class ProjectPlan(BaseModel):
    name: str = Field(description="The name of the project")
    description: str = Field(description="The description of the project")
    goals: list[str] = Field(description="The goals of the project")
    teams: list[TeamPlan] = Field(description="The teams involved in the project")