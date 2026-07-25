from hashlib import sha256
from fastapi import Request
from mcp.server.fastmcp import FastMCP
from mcp.server.context import get_request

EMAIL = "23f2000333@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-server")


@mcp.tool()
async def solve_challenge() -> str:
    request: Request = get_request()

    challenge = request.headers.get("X-Exam-Challenge")
    if not challenge:
        return "missing-challenge"

    return sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()[:16]


app = mcp.http_app()
