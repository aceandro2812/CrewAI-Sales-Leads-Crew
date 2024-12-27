# Sales Research Agent

This project uses the CrewAI framework to create a sales development representative agent that researches potential clients.

## Overview

The `crewai_sales_agent.py` script defines a sales agent that uses a search tool to identify and research potential companies. The agent is tasked with finding companies that could benefit from a specific product within a target industry. The script then outputs a markdown report to `sales_research.md` with the findings.

## Files

- `crewai_sales_agent.py`: Contains the main script for creating and running the sales agent.
- `sales_research.md`: The output file containing the sales research report.
- `readme.md`: This file, providing an overview of the project.

## How to Run

1.  Ensure you have Python installed.
2.  Install the required packages:
    ```bash
    pip install crewai pydantic langchain-community
    ```
3.  Set the `GOOGLE_API_KEY` environment variable.
4.  Run the script:
    ```bash
    python crewai_sales_agent.py
    ```

## Output

The script will generate a `sales_research.md` file containing the research results.

## Configuration

- The `crewai_sales_agent.py` script can be configured to change the target industry and product.
- The agent's role, goal, and backstory can be modified to suit different sales strategies.

## Dependencies

-   crewai
-   pydantic
-   langchain-community

## License

This project is licensed under the MIT License.
