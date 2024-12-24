from crewai import Agent, Task
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Securely load the API key from environment variables
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Define the Gemini LLM
gemini_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Create a sales agent
sales_agent = Agent(
    role='Sales Development Representative',
    goal='Identify potential customers and qualify leads for our product using provided information and tools.',
    backstory="""You are an experienced SDR with a knack for finding the right people
    and understanding their needs. You are excellent at initiating conversations and
    gathering key information. Focus on understanding the prospect's pain points and how our product can address them.""",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False # Set to False for individual agent execution
)

# Example of a task for the sales agent
research_task = Task(
    description="""Identify three potential companies that would benefit from our product.
    Focus on companies in the [target industry] and look for specific pain points our product solves.""",
    agent=sales_agent
)

if __name__ == '__main__':
    print("Sales agent created!")
    print(f"Role: {sales_agent.role}")
    print(f"Goal: {sales_agent.goal}")

    # Example of executing a task (you would typically use a Crew to orchestrate tasks)
    print("\nExecuting a sample research task:")
    research_result = research_task.execute()
    print(f"\nResearch Task Result:\n{research_result}")
