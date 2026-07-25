import inspect
from fastapi import FastAPI
from mcp.server.fastmcp import FastMCP

app = FastAPI()

@app.get("/")
def info():
    return {
        "FastMCP_methods": sorted(
            x for x in dir(FastMCP) if not x.startswith("_")
        )
    }
