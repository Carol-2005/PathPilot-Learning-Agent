# import sys
# import os
# from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


# def get_search_toolset() -> MCPToolset:
#     """
#     Launches the MCP server as a subprocess and returns a toolset
#     that ADK can give to the agent.
    
#     StdioServerParameters tells ADK:
#       - which command to run (python)
#       - which script to run (our server.py)
#       - what environment variables to pass (the SERPAPI_KEY)
#     """
#     return MCPToolset(
#         connection_params=StdioServerParameters(
#             command="python",
#             args=[
#                 # Absolute path to server.py — finds it no matter where you run from
#                 os.path.join(
#                     os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
#                     "mcp_server",
#                     "server.py"
#                 )
#             ],
#             env={
#                 # Pass secrets to the subprocess
#                 "SERPAPI_KEY": os.getenv("SERPAPI_KEY", ""),
#                 "PATH": os.environ.get("PATH", ""),
#             }
#         )
#     )
import sys
import os
from pathlib import Path
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters


def get_search_toolset() -> MCPToolset:
    # Works both locally and inside Docker (/app/mcp_server/server.py)
    server_path = Path(__file__).parent.parent / "mcp_server" / "server.py"

    return MCPToolset(
        connection_params=StdioServerParameters(
            command=sys.executable,
            args=[str(server_path)],
            env={
                "SERPAPI_KEY": os.getenv("SERPAPI_KEY", ""),
                "PATH": os.environ.get("PATH", ""),
                "PYTHONPATH": os.environ.get("PYTHONPATH", ""),
            }
        )
    )