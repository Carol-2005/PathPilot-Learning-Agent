# PathPilot 🚀

Constraint-Aware Learning Path Optimizer

## Problem

Finding learning resources online leads to overload, inconsistent quality, and no clear structure. Existing tools return links, not optimized learning paths.

## Solution

PathPilot is an AI agent that:

* retrieves real-time learning resources
* filters and evaluates them
* generates structured, personalized learning paths based on constraints

## Architecture

User → ADK Agent (Gemini) → MCP Server → SerpAPI → Structured Plan

## Tech Stack

* Google ADK (Agent framework)
* Gemini (LLM)
* FastMCP (tool server)
* SerpAPI (search)
* Docker (deployment)

## Project Structure

```
pathpilot/
├── pathpilot/
│   ├── agent.py
│   ├── tools.py
│   └── __init__.py
├── mcp_server/
│   └── server.py
├── requirements.txt
├── .env
└── Dockerfile
```

## Setup

### 1. Create environment

```bash
python -m venv venv
```


## Example Prompt

```
I want to learn machine learning. I’m a beginner, have 6 hours/week,
prefer videos, and want to build projects.
```

## Output

* Structured learning phases
* Curated resources with links
* Time-based progression
* Milestones

---

