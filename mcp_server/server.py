import os
import requests
from fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()

# FastMCP creates an MCP-compliant server with one line
# "PathPilot Resources" is just a display name
mcp = FastMCP("PathPilot Resources")

SERPAPI_KEY = os.getenv("SERPAPI_KEY")


@mcp.tool()
def search_learning_resources(
    topic: str,
    skill_level: str = "beginner",
    max_results: int = 8
) -> list[dict]:
    """
    Search for learning resources on a given topic.
    
    Args:
        topic: The subject to learn (e.g. "Python async programming")
        skill_level: One of beginner / intermediate / advanced
        max_results: How many results to return (default 8)
    
    Returns:
        A list of dicts with title, url, snippet, and source fields.
    """
    query = f"{skill_level} {topic} tutorial course learning resource"
    
    params = {
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": max_results,
        "engine": "google",
    }

    response = requests.get("https://serpapi.com/search", params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("organic_results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", ""),
            "source": item.get("displayed_link", ""),
        })

    return results


if __name__ == "__main__":
    # stdio mode — ADK talks to this server via standard input/output
    mcp.run(transport="stdio")