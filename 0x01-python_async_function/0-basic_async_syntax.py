#!/usr/bin/env python3
"""
This module demonstrates async/await briefly works
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns random delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
