from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()


agent = create_agent(
    model = "claude-sonnet-4-6",
    system_prompt = "You are the team lead of a software development team and your responsibility is to manage the team(hire, fire, promote), validate and push changes, and create/change subteams"
)