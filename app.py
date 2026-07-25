from fastapi import FastAPI
import mcp.server.fastmcp as fm

app = FastAPI()

@app.get("/")
def info():
    return {
        "module": sorted(x for x in dir(fm) if not x.startswith("_"))
    }
