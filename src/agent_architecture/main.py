from agents.main_agent import agent

if __name__ == "__main__":
    user_prompt = input("Enter your dev prompt: ")
    print("user input: ", user_prompt)

    response = agent.invoke(
        {"messages":[{"role": "user", "content": user_prompt}]}
    )
    print("agent response: ", response["messages"][-1].content_blocks)

    
