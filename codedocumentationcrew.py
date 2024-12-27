from crewai import Agent, Task, Crew , Process ,LLM
import os
from typing import List, Dict
from pydantic import BaseModel, Field

gemini_llm  = LLM(
    model="openai/gemini-2.0-flash-exp",
    temperature=0.7,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key="AIzaSyA6Gd_kJL0g8XCMZXJ-uJwbTDYcac1zqGk"
)

Directory_agent = Agent(
    role='Codebase Analysis Agent',
    goal='Identify potential customers and qualify leads for our product using provided information and tools.',
    backstory="""You are an experienced SDR with a knack for finding the right people
    and understanding their needs. You are excellent at initiating conversations and
    gathering key information. Focus on understanding the prospect's pain points and how our product can address them.""",
    llm=gemini_llm,
    tools=[search_tool],
    verbose=True,
    allow_delegation=False
)