"""
Local Study & Lab Workspace MCP Assistant
Author: Abdul Moiz Satti
Track: General AI Fluency Capstone
"""

import os
import sys
import json
import re
from pathlib import Path

SAFE_DIR = Path.home() / "lab_workspace"

def sanitize_path(target_path: str) -> Path:
    """Enforce strict directory traversal containment."""
    resolved = (SAFE_DIR / target_path).resolve()
    if not str(resolved).startswith(str(SAFE_DIR.resolve())):
        raise PermissionError(f"Security Alert: Directory traversal detected -> {target_path}")
    return resolved

def index_notes_tool(query: str) -> list:
    """Scans and indexes local Markdown lab notes without external network calls."""
    SAFE_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    clean_query = re.escape(query.lower())
    
    for file_path in SAFE_DIR.glob("**/*.md"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                if re.search(clean_query, content.lower()):
                    results.append({
                        "file": file_path.name,
                        "snippet": content[:200] + "..."
                    })
        except Exception as e:
            continue
    return results

def handle_mcp_request(raw_payload: str) -> str:
    """Process incoming JSON-RPC formatted stdio MCP requests."""
    try:
        data = json.loads(raw_payload)
        method = data.get("method")
        params = data.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "tools": [{
                    "name": "index_notes",
                    "description": "Searches and indexes local markdown lab workspace notes.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {"type": "string", "description": "Search term or tag"}
                        },
                        "required": ["query"]
                    }
                }]
            })
            
        elif method == "tools/call" and params.get("name") == "index_notes":
            search_res = index_notes_tool(params.get("arguments", {}).get("query", ""))
            return json.dumps({"result": search_res})
            
        return json.dumps({"error": "Unsupported tool or method"})
    except Exception as err:
        return json.dumps({"error": str(err)})

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Verification self-test
        sample_call = json.dumps({"method": "tools/list"})
        print("MCP Self-Test Output:", handle_mcp_request(sample_call))
    else:
        # Standard MCP stdio loop
        for line in sys.stdin:
            if line.strip():
                print(handle_mcp_request(line.strip()))
                sys.stdout.flush()
