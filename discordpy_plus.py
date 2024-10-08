import aiohttp
import asyncio
import json

async def get_httpcat(数字: int):
  return f"https://http.cat/{数字}"