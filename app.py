from fastapi import FastAPI
import importlib.metadata

app = FastAPI()

@app.get("/")
def version():
    return {
        "mcp_version": importlib.metadata.version("mcp")
    }
