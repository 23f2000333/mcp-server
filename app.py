from hashlib import sha256

from fastapi import Request
from mcp.server.fastmcp import FastMCP, Context

EMAIL = "23f2000333@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("exam-server")


@mcp.tool()
async def solve_challenge(ctx: Context) -> str:
    request: Request = ctx.request

    challenge = request.headers.get("X-Exam-Challenge")
    if challenge is None:
        return "missing-challenge"

    return sha256(
        f"{challenge}:{EMAIL}".encode()
    ).hexdigest()[:16]


app = mcp.streamable_http_app()
