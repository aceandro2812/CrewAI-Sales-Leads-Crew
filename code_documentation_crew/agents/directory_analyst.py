from crewai import Agent
from tools.directory_rag import DirectoryRAGTool

class DirectoryAnalyst(Agent):
    """
    An agent responsible for analyzing the directory structure of a code repository.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tools = [DirectoryRAGTool()]
        self.role = "Directory Analyst"
        self.goal = "Analyze the directory structure of a code repository and identify all relevant source code files and subdirectories."
        self.backstory = "You are an expert in software project structure and understand how to navigate code repositories."
