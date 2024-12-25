from crewai import Task
from agents.directory_analyst import DirectoryAnalyst

class AnalyzeDirectory(Task):
    """
    A task for analyzing the directory structure of a code repository.
    """
    def __init__(self, directory_path, **kwargs):
        super().__init__(**kwargs)
        self.agent = DirectoryAnalyst()
        self.description = f"Analyze the directory structure at {directory_path} and identify all relevant source code files and subdirectories."
        self.directory_path = directory_path
