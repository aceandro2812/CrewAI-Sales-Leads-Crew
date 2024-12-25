import os
from crewai import BaseTool

class DirectoryRAGTool(BaseTool):
    """
    A tool for analyzing the directory structure of a code repository.
    """
    def __init__(self):
        super().__init__()
        self.description = "Useful for when you need to analyze the directory structure of a code repository."

    def _run(self, directory_path):
        """
        Analyzes the directory structure of a code repository.

        Args:
            directory_path (str): The path to the directory to analyze.

        Returns:
            str: A string containing the list of files and directories.
        """
        try:
            items = os.listdir(directory_path)
            files = [item for item in items if os.path.isfile(os.path.join(directory_path, item))]
            directories = [item for item in items if os.path.isdir(os.path.join(directory_path, item))]
            return f"Files: {files}\nDirectories: {directories}"
        except Exception as e:
            return f"Error analyzing directory: {e}"
