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
    goal='Qualify leads and schedule meetings with potential customers.',
    backstory="""You are an experienced SDR who excels at engaging potential customers
    and identifying their specific needs. You are skilled at asking targeted questions
    and setting up qualified meetings for the sales team.""",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=False
)

# Create a lead sales agent
lead_sales_agent = Agent(
    role='Lead Generation Specialist',
    goal='Identify and research potential companies that would benefit from our product.',
    backstory="""You are a highly effective lead generation specialist with a deep understanding
    of market research and identifying ideal customer profiles. You are adept at finding
    key information about companies and their potential pain points.""",
    llm=gemini_llm,
    verbose=True,
    allow_delegation=True
)

# Example of tasks for the agents
research_task = Task(
    description="""Identify three potential companies that would benefit from our product.
    Focus on companies in the [target industry] and look for specific pain points our product solves.
    Provide a brief summary of each company and why they are a good fit.""",
    agent=lead_sales_agent
)

qualification_task = Task(
    description="""Based on the list of companies provided by the Lead Generation Specialist,
    select the most promising lead and find the contact information for the appropriate decision-maker.
    Prepare a brief initial outreach message highlighting how our product can address their needs.""",
    agent=sales_agent,
    context=[research_task]
)

# Create a sales crew
sales_crew = Crew(
    agents=[lead_sales_agent, sales_agent],
    tasks=[research_task, qualification_task],
    verbose=2
)

if __name__ == '__main__':
    print("Sales agents created!")
    print(f"Lead Sales Agent Role: {lead_sales_agent.role}")
    print(f"Lead Sales Agent Goal: {lead_sales_agent.goal}")
    print(f"Sales Agent Role: {sales_agent.role}")
    print(f"Sales Agent Goal: {sales_agent.goal}")

    print("\nExecuting the sales process with the crew:")
    result = sales_crew.kickoff()
    print(f"\nSales Process Result:\n{result}")
