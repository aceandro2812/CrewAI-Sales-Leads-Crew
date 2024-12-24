# AI: refactor this code looking at the crew ai documentation
import os
from crewai import Agent
from langchain_google_genai import ChatGoogleGenerativeAI

os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY"  # Replace with your actual API key

# Define the Gemini LLM
gemini_llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Create a sales agent
sales_agent = Agent(
    role='Sales Development Representative',
    goal='Identify potential customers and qualify leads for our product',
    backstory="""You are an experienced SDR with a knack for finding the right people 
    and understanding their needs. You are excellent at initiating conversations and 
    gathering key information.""",
    llm=gemini_llm,
    verbose=True
)

if __name__ == '__main__':
    print("Sales agent created!")
    print(f"Role: {sales_agent.role}")
    print(f"Goal: {sales_agent.goal}")
