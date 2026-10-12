from agent_architecture.agents.main_agent import agent
from src.agent_architecture.services.organization_builder import OrganizationBuilder

if __name__ == "__main__":
    user_prompt = input("Enter your dev prompt: ")
    print("user input: ", user_prompt)

    response = agent.invoke(
        {"messages":[{"role": "user", "content": user_prompt}]}
    )
    project_plan = response["structured_response"]
    print(type(project_plan))
    project = OrganizationBuilder(project_plan).make_project()

    print(project.name)
    for team in project.teams:
        print(f"Team: {team.name}")
    for agent in team.members:
        print(f"Agent: {agent.name}")


