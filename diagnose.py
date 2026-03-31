import sys
import os
import subprocess
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

print("=" * 50)
print("1. Python executable:")
print("  ", sys.executable)

print("\n2. Working directory:")
print("  ", os.getcwd())

print("\n3. server.py path:")
server_path = Path("mcp_server") / "server.py"
print("  ", server_path.absolute())
print("   exists:", server_path.exists())

print("\n4. Environment variables:")
print("   SERPAPI_KEY set:", bool(os.getenv("SERPAPI_KEY")))
print("   GOOGLE_API_KEY set:", bool(os.getenv("GOOGLE_API_KEY")))

print("\n5. Testing server.py imports:")
result = subprocess.run(
    [sys.executable, "-c", 
     "from fastmcp import FastMCP; from dotenv import load_dotenv; import requests; print('ALL IMPORTS OK')"],
    capture_output=True, text=True
)
print("  ", result.stdout.strip() or result.stderr.strip())

print("\n6. Testing MCP server handshake:")
import json, threading, time

proc = subprocess.Popen(
    [sys.executable, str(server_path.absolute())],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    env={**os.environ, "SERPAPI_KEY": os.getenv("SERPAPI_KEY", "")}
)

# Send MCP initialize message
init_msg = json.dumps({
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "test", "version": "1.0"}
    }
}) + "\n"

try:
    proc.stdin.write(init_msg)
    proc.stdin.flush()
    time.sleep(2)
    output = proc.stdout.readline()
    print("   Server response:", output.strip() if output else "NO RESPONSE")
    err = proc.stderr.read1(1024) if hasattr(proc.stderr, 'read1') else ""
    if err:
        print("   Server stderr:", err)
except Exception as e:
    print("   Error:", e)
finally:
    proc.terminate()

print("\n7. agent.py imports:")
result2 = subprocess.run(
    [sys.executable, "-c",
     "import sys; sys.path.insert(0, '.'); from pathpilot.agent import root_agent; print('root_agent OK:', root_agent.name)"],
    capture_output=True, text=True
)
print("  ", result2.stdout.strip() or result2.stderr.strip())

print("=" * 50)