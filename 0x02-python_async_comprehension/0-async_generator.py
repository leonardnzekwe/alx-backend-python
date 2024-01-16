#!/usr/bin/env python3
"""
Asynchronous generator that yields random numbers between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """
    Coroutine that loops 10 times,
    asynchronously waits for 1 second, and yields
    a random number between 0 and 10 each time.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
