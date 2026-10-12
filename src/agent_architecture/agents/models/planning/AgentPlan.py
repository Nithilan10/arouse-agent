from pydantic import BaseModel, Field

class AgentPlan(BaseModel):
    name: str = Field(description="The name of the agent")
    role: str = Field(description="The role of the agent in the project")
    responsibilities: list[str] = Field(description="The responsibilities of the agent in the project")
    capabilities: list[str] = Field(description="The capabilities of the agent in the project")
    required_tools: list[str] = Field(description="The tools required for the agent to perform their role")