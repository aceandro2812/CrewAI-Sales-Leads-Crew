from crewai import Agent, Task, Crew , Process ,LLM
import os
# from langchain_google_genai import ChatGoogleGenerativeAI

# Securely load the API key from environment variables
# os.environ["GOOGLE_API_KEY"] = "AIzaSyA6Gd_kJL0g8XCMZXJ-uJwbTDYcac1zqGk"

# Define the Gemini LLM
gemini_llm  = LLM(
    model="openai/gemini-2.0-flash-exp",
    temperature=0.7,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key="AIzaSyA6Gd_kJL0g8XCMZXJ-uJwbTDYcac1zqGk"
)

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
    description="""
    ## Objective:
    Identify and research three potential companies within a specified target industry that could significantly benefit from our product.

    ## Target Industry:
    Focus on companies operating in the {target_industry}.

    ## Product:
    Our product, {product}, offers a unique solution to common industry challenges.

    ## Research Guidelines:
    For each company, conduct a thorough analysis to identify specific pain points and challenges that our product is designed to address. Consider the following aspects:
    - **Company Profile:** Size, revenue, market position, and growth trajectory.
    - **Current Challenges:** Any known issues or areas where the company is struggling or seeking improvement.
    - **Product-Solution Fit:** How our product's features and capabilities can directly address these challenges and provide tangible benefits.

    ## Output Format:
    Provide a detailed report for each company, including:
    - **Company Name:**
    - **Industry:**
    - **Pain Points:** A list of identified challenges.
    - **Solution Fit:** A clear explanation of how our product can solve these pain points.
    - **Reasoning:** A brief justification for why this company is a good fit for our product.

    ## Constraints:
    - Focus exclusively on the specified target industry.
    - Ensure that the identified pain points are relevant to the solutions offered by our product.
    - Base your research on publicly available information and avoid any confidential or proprietary data.

    This detailed analysis will enable our sales team to tailor their approach and effectively communicate the value proposition of our product to each potential client.""",
    agent=sales_agent,
    expected_output="A markdown report containing a list of three companies, each with their identified pain points, how the product addresses them, and a justification for why each company is a good fit.",
    output_file="sales_research.md"
)

# Create a Crew to manage the agent and tasks
sales_crew = Crew(
    agents=[sales_agent],
    tasks=[research_task],
    process=Process.sequential,
)

if __name__ == '__main__':
    print("Sales agent created!")
    print(f"Role: {sales_agent.role}")
    print(f"Goal: {sales_agent.goal}")

    # Execute the tasks using the Crew's kickoff method
    print("\nExecuting the sales process with the crew:")
    result = sales_crew.kickoff(
        inputs={
            "target_industry": "Societies and Chartered Accountants in Mumbai Region",
            "product": "Society Register Management System"
        }
    )
    print(f"\nSales Process Result:\n{result}")
