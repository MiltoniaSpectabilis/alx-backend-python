#!/usr/bin/env python3

"""
Module for an async generator that yields random numbers.
"""

import asyncio
import random


async def async_generator():
    """
    Yields a random number between 0 and 10 after waiting 1 second, 10 times.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
