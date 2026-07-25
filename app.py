from hashlib import sha256

from fastapi import FastAPI, Request
from mcp.server.fastmcp import FastMCP

EMAIL = "23f2000333@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-server")


@mcp.tool()
async def solve_challenge() -> str:
    """
    The challenge is supplied via HTTP headers.
    """
    # FastMCP injects the Starlette request into the context
    from mcp.server.context import get_request

    request: Request = get_request()

    challenge = request.headers.get("X-Exam-Challenge")

    if challenge is None:
        return "missing-challenge"

    answer = sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()[:16]

    return answer


app = FastAPI()

app.mount("/mcp", mcp.streamable_http_app())
