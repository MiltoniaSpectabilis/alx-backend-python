#!/usr/bin/env python3
"""
This script demonstrates how async/await works
"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in tasks]
    return delays
