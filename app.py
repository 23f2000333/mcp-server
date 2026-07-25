from fastapi import FastAPI
import inspect
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("exam")
app = FastAPI()

@app.get("/")
def sig():
    return {
        "signature": str(inspect.signature(mcp.streamable_http_app))
    }
