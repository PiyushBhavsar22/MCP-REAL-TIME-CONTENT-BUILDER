from mcp.server.fastmcp import FastMCP
from app import get_realtime_info, generate_video_transcription

mcp = FastMCP("This is for the Script generator")

async def get_latest_info_mcp(query):
    return get_realtime_info(query)

async def get_video_script_mcp(query):
    real_info = generate_video_transcription(query)
    return generate_video_transcription(real_info)

if __name__ == "__main__":
    mcp.run(transport="stdio")