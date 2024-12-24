from crewai import Agent, Task, Crew
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
    Focus on companies in the {target_industry} and look for specific pain points {product} solves.""",
    agent=sales_agent
)

# Create a Crew to manage the agent and tasks
sales_crew = Crew(
    agents=[sales_agent],
    tasks=[research_task],
    verbose=2  # You can adjust verbosity for more detailed output
)

if __name__ == '__main__':
    print("Sales agent created!")
    print(f"Role: {sales_agent.role}")
    print(f"Goal: {sales_agent.goal}")

    # Execute the tasks using the Crew's kickoff method
    print("\nExecuting the sales process with the crew:")
    result = sales_crew.kickoff(
        inputs={
            "target_industry": "SaaS",
            "product": "AI-powered chatbot platform"
        }
    )
    print(f"\nSales Process Result:\n{result}")
